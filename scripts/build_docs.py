#!/usr/bin/env python3
"""Stage source Markdown files for the MkDocs build."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
DOCS_STAGING = ROOT / "docs-staging"


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> None:
    if DOCS_STAGING.exists():
        shutil.rmtree(DOCS_STAGING)

    DOCS_STAGING.mkdir()
    copy_file(ROOT / "README.md", DOCS_STAGING / "index.md")
    copy_file(ROOT / "overview.md", DOCS_STAGING / "overview.md")

    techniques_dir = ROOT / "techniques"
    for markdown_file in sorted(techniques_dir.glob("*.md")):
        copy_file(markdown_file, DOCS_STAGING / "techniques" / markdown_file.name)

    print(f"Staged documentation in {DOCS_STAGING.relative_to(ROOT)}")


if __name__ == "__main__":
    main()