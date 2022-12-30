"""Main plugin module."""

import argparse
from pathlib import Path
from typing import Mapping

from markdown_it import MarkdownIt
from mdformat import _conf
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

_conf_validate_values = _conf._validate_values


def _validate_values(opts: Mapping, conf_path: Path) -> None:
    _conf_validate_values(opts, conf_path)
    wrap = opts.get("wrap")
    if not isinstance(wrap, int):
        wrap = 70

    character = opts.get("thematic_breaks_character")
    if character not in (None, "-", "_", "*"):
        raise _conf.InvalidConfError(
            f"Invalid 'thematic_breaks_character' value in {conf_path}: {character}"
        )

    length = opts.get("thematic_breaks_length")
    if length is not None and not (isinstance(length, int) and 3 <= length <= wrap):
        raise _conf.InvalidConfError(
            f"Invalid 'thematic_breaks_length' value in {conf_path}: {length}"
        )


def _monkey_patch_mdformat_on_import() -> None:
    """Monkey patch the mdformat._conf to add the plugin opts.`"""
    _conf.DEFAULT_OPTS["thematic_breaks_character"] = "-"
    _conf.DEFAULT_OPTS["thematic_breaks_length"] = 3
    _conf._validate_values = _validate_values


def thematic_break_length(value: str) -> int:
    value = int(value)
    if value < 3:
        raise ValueError("thematic_break_length must be an integer greater than 2")

    return value


def add_cli_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--thematic-breaks-character",
        choices=("-", "_", "*"),
        help="Character to use for rendering thematic breaks (default: -)",
    )
    parser.add_argument(
        "--thematic-breaks-length",
        type=thematic_break_length,
        help="Length of the rendered thematic breaks (default: 3)",
    )


def update_mdit(mdit: MarkdownIt) -> None:
    """No-op update_mdit for mdformat-simple-breaks plugin."""
    pass


def hr(node: RenderTreeNode, context: RenderContext) -> str:
    character = context.options["mdformat"]["thematic_breaks_character"]
    length = context.options["mdformat"]["thematic_breaks_length"]
    return character * length


RENDERERS: Mapping[str, Render] = {"hr": hr}


_monkey_patch_mdformat_on_import()
