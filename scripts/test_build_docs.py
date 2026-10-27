from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_docs


class DiagramEmbeddingTests(unittest.TestCase):
    def test_embeds_figures_at_both_document_depths(self):
        with tempfile.TemporaryDirectory() as directory:
            diagrams = Path(directory)
            figure = '<figure class="site-diagram"><svg></svg></figure>'
            (diagrams / "example.html").write_text(
                f"<!DOCTYPE html><html><body>{figure}</body></html>",
                encoding="utf-8",
            )
            with patch.object(build_docs, "DIAGRAMS", diagrams):
                for prefix in ("", "../"):
                    with self.subTest(prefix=prefix):
                        source = (
                            f"Before\n\n[Diagram: Example]({prefix}diagrams/example.html)"
                            "\n\nAfter\n"
                        )
                        self.assertEqual(
                            build_docs.embed_diagrams(source),
                            f"Before\n\n{figure}\n\nAfter\n",
                        )

    def test_leaves_other_links_and_markdown_unchanged(self):
        source = (
            "# Example\n\n[Ordinary link](diagrams/example.html)\n"
            "[Diagram: Invalid path](diagrams/../../example.html)\n"
        )
        self.assertEqual(build_docs.embed_diagrams(source), source)

    def test_missing_diagram_fails_build(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(build_docs, "DIAGRAMS", Path(directory)):
                with self.assertRaises(FileNotFoundError):
                    build_docs.embed_diagrams("[Diagram: Missing](diagrams/missing.html)")

    def test_missing_figure_fails_build(self):
        with tempfile.TemporaryDirectory() as directory:
            diagrams = Path(directory)
            (diagrams / "empty.html").write_text("<html></html>", encoding="utf-8")
            with patch.object(build_docs, "DIAGRAMS", diagrams):
                with self.assertRaisesRegex(ValueError, "No figure"):
                    build_docs.embed_diagrams("[Diagram: Empty](diagrams/empty.html)")


if __name__ == "__main__":
    unittest.main()
