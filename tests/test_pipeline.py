from pathlib import Path

from openstyle.pipeline import OpenStylePipeline


def test_analyze_and_generate_moban2603(tmp_path: Path) -> None:
    template_dir = Path(r"E:\OpenStyle\3C数码电子产品网站模板_www.mobancss.com\moban2603")
    pipeline = OpenStylePipeline(base_dir=Path(__file__).resolve().parents[1] / "src" / "openstyle")
    out = pipeline.generate_all(template_dir, tmp_path)
    assert (out / "DESIGN.md").exists()
    assert (out / "preview.html").exists()
    assert (out / "preview-dark.html").exists()
    text = (out / "DESIGN.md").read_text(encoding="utf-8")
    assert "## 2. Color Palette & Roles" in text


def test_analyze_moban4024_tokens() -> None:
    template_dir = Path(r"E:\OpenStyle\花草植物种植HTML5模板_www.mobancss.com\moban4024")
    pipeline = OpenStylePipeline(base_dir=Path(__file__).resolve().parents[1] / "src" / "openstyle")
    tokens = pipeline.analyze_template(template_dir)
    assert tokens.template_name
    assert tokens.colors
    assert tokens.typography
