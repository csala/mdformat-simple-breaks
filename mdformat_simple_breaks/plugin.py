"""Main plugin module."""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Mapping

    from markdown_it import MarkdownIt
    from mdformat.renderer import RenderContext, RenderTreeNode
    from mdformat.renderer.typing import Render


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    pass


def hr(node: RenderTreeNode, context: RenderContext) -> str:
    return "---"


RENDERERS: Mapping[str, Render] = {"hr": hr}
