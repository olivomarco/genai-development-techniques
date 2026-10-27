#!/usr/bin/env python3
"""Stage source Markdown files for the MkDocs build."""

from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
DOCS_STAGING = ROOT / "docs-staging"
DIAGRAMS = ROOT / "diagrams"
DIAGRAM_LINK = re.compile(
    r"^\[Diagram: [^\]\n]+\]\((?:\.\./)?diagrams/([a-z0-9-]+)\.html\)[ \t]*$",
    re.MULTILINE,
)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def embed_diagrams(markdown: str) -> str:
    def replace(match: re.Match[str]) -> str:
        source = DIAGRAMS / f"{match[1]}.html"
        diagram = source.read_text(encoding="utf-8")
        figure = re.search(r"<figure\b[^>]*>.*?</figure>", diagram, re.DOTALL)
        if figure is None:
            raise ValueError(f"No figure found in {source}")
        return figure[0]

    return DIAGRAM_LINK.sub(replace, markdown)


def stage_markdown(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        embed_diagrams(source.read_text(encoding="utf-8")), encoding="utf-8"
    )


def main() -> None:
    if DOCS_STAGING.exists():
        shutil.rmtree(DOCS_STAGING)

    DOCS_STAGING.mkdir()
    stage_markdown(ROOT / "README.md", DOCS_STAGING / "index.md")
    stage_markdown(ROOT / "overview.md", DOCS_STAGING / "overview.md")
    stage_markdown(ROOT / "methodology.md", DOCS_STAGING / "methodology.md")

    techniques_dir = ROOT / "techniques"
    for markdown_file in sorted(techniques_dir.glob("*.md")):
        stage_markdown(markdown_file, DOCS_STAGING / "techniques" / markdown_file.name)

    for diagram in sorted(DIAGRAMS.glob("*.html")):
        copy_file(diagram, DOCS_STAGING / "diagrams" / diagram.name)

    print(f"Staged documentation in {DOCS_STAGING.relative_to(ROOT)}")


if __name__ == "__main__":
    main()