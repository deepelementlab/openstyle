from __future__ import annotations

from pathlib import Path

import click

from openstyle.pipeline import OpenStylePipeline
from openstyle.naming import (
    bundle_english_labels,
    shorten_filesystem_slug,
    strip_mobancss_bundle_suffix,
    unique_slug,
)


SKIP_ROOT_DIR_NAMES = frozenset({"ui", "openstyle", ".git", ".cursor", "node_modules", ".venv", "__pycache__"})

# When walking inside a bundle, skip common junk path segments (lowercased).
SKIP_INNER_PATH_PARTS = frozenset(
    {
        "openstyle",
        ".git",
        "node_modules",
        "__pycache__",
        ".venv",
    }
)

# Nested vendor / demo trees often contain index.html; skip those as template roots.
_BAD_INDEX_DIR_SEGMENTS = frozenset(
    {
        "source",
        "vendor",
        "vendors",
        "node_modules",
        "bower_components",
        "documentation",
        "docs",
        "examples",
        "example",
        "demos",
        "demo",
        "tests",
        "test",
        "coverage",
        ".git",
    }
)
_MAX_INDEX_REL_PARTS = 6  # e.g. bundle / theme / sub / index.html


@click.group()
def cli() -> None:
    """OpenStyle 命令行工具。"""


@cli.command()
@click.argument("template_dir", type=click.Path(exists=True, path_type=Path))
@click.option("-o", "--output", type=click.Path(path_type=Path), default=Path("./output"))
def analyze(template_dir: Path, output: Path) -> None:
    """分析单个模板并生成 DESIGN.md / preview 文件。"""
    pipeline = OpenStylePipeline()
    target = pipeline.generate_all(template_dir, output)
    click.echo(f"Generated: {target}")


@cli.command()
@click.argument("root_dir", type=click.Path(exists=True, path_type=Path))
@click.option("-o", "--output", type=click.Path(path_type=Path), default=Path("./output"))
def batch(root_dir: Path, output: Path) -> None:
    """批量扫描模板目录（含 index.html）并生成输出。"""
    pipeline = OpenStylePipeline()
    count = 0
    for index in root_dir.rglob("index.html"):
        template_dir = index.parent
        if any(part.lower() == "ui" for part in template_dir.parts):
            continue
        try:
            target = pipeline.generate_all(template_dir, output)
            click.echo(f"[OK] {template_dir} -> {target}")
            count += 1
        except Exception as exc:  # noqa: BLE001
            click.echo(f"[SKIP] {template_dir} ({exc})")
    click.echo(f"Completed. Generated {count} templates.")


@cli.command()
@click.argument("design_md", type=click.Path(exists=True, path_type=Path))
@click.option("-o", "--output", type=click.Path(path_type=Path), default=None)
def preview(design_md: Path, output: Path | None) -> None:
    """基于 DESIGN.md 仅生成预览页面。"""
    pipeline = OpenStylePipeline()
    target = output or design_md.parent
    generated = pipeline.generate_preview_from_design(design_md, target)
    click.echo(f"Generated preview files in: {generated}")


def _path_has_skipped_part(path: Path, bundle_root: Path) -> bool:
    """Skip only if a blocked segment appears *inside* the bundle (not the host folder name)."""
    try:
        rel = path.resolve().relative_to(bundle_root.resolve())
    except ValueError:
        return True
    lowered = {p.casefold() for p in rel.parts}
    return bool(lowered & {s.casefold() for s in SKIP_INNER_PATH_PARTS})


def _is_under(path: Path, ancestor: Path) -> bool:
    try:
        path.resolve().relative_to(ancestor.resolve())
        return True
    except ValueError:
        return False


def _index_is_plausible_template_root(index_path: Path, bundle_root: Path) -> bool:
    """Reject vendor/demo/source trees that ship sample index.html files."""
    try:
        rel = index_path.resolve().relative_to(bundle_root.resolve())
    except ValueError:
        return False
    if len(rel.parts) > _MAX_INDEX_REL_PARTS:
        return False
    dir_parts_cf = {p.casefold() for p in rel.parts[:-1]}
    bad_cf = {s.casefold() for s in _BAD_INDEX_DIR_SEGMENTS}
    return not (dir_parts_cf & bad_cf)


def _iter_bundle_index_files(bundle: Path) -> list[Path]:
    """Collect index.html / index.htm under a bundle (deduped by resolved path)."""
    paths: list[Path] = []
    for pattern in ("index.html", "index.htm", "Index.html", "INDEX.HTML"):
        paths.extend(bundle.rglob(pattern))
    seen: set[Path] = set()
    out: list[Path] = []
    for p in paths:
        if p.name.casefold() not in ("index.html", "index.htm"):
            continue
        r = p.resolve()
        if r not in seen:
            seen.add(r)
            out.append(p)
    return out


@cli.command("batch-openstyle")
@click.argument("openstyle_root", type=click.Path(exists=True, path_type=Path))
@click.option("-o", "--output", type=click.Path(path_type=Path), default=Path(r"E:\OpenStyle\UI"))
@click.option(
    "--cache",
    type=click.Path(path_type=Path),
    default=None,
    help="JSON cache for zh->English title+slug (default: <openstyle_root>/.openstyle-bundle-labels.json)",
)
@click.option("--no-translate", is_flag=True, help="Do not call online translation; use pinyin-based slug/title.")
@click.option("--sleep", "sleep_s", type=float, default=0.15, help="Seconds to sleep after each translation call.")
@click.option(
    "--skip-existing",
    is_flag=True,
    help="Skip when DESIGN.md already exists for output/<slug>/<template-folder> (for incremental runs).",
)
def batch_openstyle(
    openstyle_root: Path,
    output: Path,
    cache: Path | None,
    no_translate: bool,
    sleep_s: float,
    skip_existing: bool,
) -> None:
    """Scan each first-level folder under OpenStyle, strip mobancss suffix, emit English slug folders.

    Output layout: OUTPUT/<english-slug>/<template-subfolder>/{DESIGN.md,preview*.html,README.md}
    """
    cache_path = cache or (openstyle_root / ".openstyle-bundle-labels.json")
    pipeline = OpenStylePipeline()
    output.mkdir(parents=True, exist_ok=True)
    used_bundle_slugs: set[str] = {p.name for p in output.iterdir() if p.is_dir()}
    generated = 0
    output_res = output.resolve()

    bundles = sorted([p for p in openstyle_root.iterdir() if p.is_dir()], key=lambda p: p.name.casefold())
    for bundle in bundles:
        if bundle.name.casefold() in {s.casefold() for s in SKIP_ROOT_DIR_NAMES}:
            continue
        indexes = [
            p
            for p in _iter_bundle_index_files(bundle)
            if _index_is_plausible_template_root(p, bundle)
            and not _path_has_skipped_part(p, bundle)
            and not _is_under(p, output_res)
        ]
        if not indexes:
            click.echo(f"[SKIP] no index.html under {bundle.name!r}")
            continue

        display_zh = strip_mobancss_bundle_suffix(bundle.name)
        title_en, slug_base = bundle_english_labels(
            display_zh,
            cache_path=cache_path,
            use_translation=not no_translate,
            sleep_s=0.0 if no_translate else sleep_s,
        )
        bundle_slug = unique_slug(slug_base, used_bundle_slugs)
        bundle_slug = shorten_filesystem_slug(
            bundle_slug,
            seed=f"{bundle.name}|{display_zh}",
            max_len=160,
        )

        seen_parents: set[Path] = set()
        for index in sorted(indexes):
            template_dir = index.parent.resolve()
            if template_dir in seen_parents:
                continue
            seen_parents.add(template_dir)
            dest = output / bundle_slug / template_dir.name
            if skip_existing and (dest / "DESIGN.md").exists():
                click.echo(f"[SKIP exists] {dest}")
                continue
            try:
                target = pipeline.generate_all(
                    template_dir,
                    output / bundle_slug,
                    output_folder_name=template_dir.name,
                    readme_bundle={
                        "bundle_folder_name": bundle.name,
                        "bundle_title_zh": display_zh,
                        "bundle_title_en": title_en,
                        "bundle_slug": bundle_slug,
                    },
                )
                click.echo(f"[OK] {template_dir} -> {target}")
                generated += 1
            except Exception as exc:  # noqa: BLE001
                click.echo(f"[SKIP] {template_dir} ({exc})")

    click.echo(f"Completed. Wrote {generated} template output folders under {output}.")
