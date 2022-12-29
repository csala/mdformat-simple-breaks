# Development Guide

## Development Setup

This package utilises [flit][flit] as the build engine, and [tox][tox] for test automation.

To install these development dependencies:

```bash
pip install tox
```

To run the tests:

```bash
tox
```

and with test coverage:

```bash
tox -e py37-cov
```

The easiest way to write tests, is to edit tests/fixtures.md

To run the code formatting and style checks:

```bash
tox -e py37-pre-commit
```

or directly

```bash
pip install pre-commit
pre-commit run --all
```

To run the pre-commit hook test:

```bash
tox -e py37-hook
```

## Publish to PyPi

Either use flit directly:

```bash
pip install flit
flit publish
```

or trigger the GitHub Action job, by creating a release with a tag equal to the version, e.g. `v0.0.1`.

Note, this requires generating an API key on PyPi and adding it to the repository `Settings/Secrets`, under the name `PYPI_KEY`.

# Plugin Architecture

The plugin simply overwrites the [`hr`][hr-code] function from the [mdformat][mdformat] library
and returns a fixed `---` string instead of the 70 `_` one.

# General Coding Guidelines

This is part of the initial development guides included in the [mdformat-plugin][mdformat-plugin]
repo and [mdformat contributing guide][mdformat-contributing]. Copied over here for reference.

## Required changes for a new plugin

This demonstration is setup with a plugin named `plugin`.
There are a number of locations to change.
At a top level for a plugin `foo` at least the following changes are required

- Global find and replace `mdformat_plugin` to `mdformat_foo` including folder names.
- Global find and replace `mdformat-plugin` to `mdformat-foo` including folder names.
- `tests/test_fixtures.py`: `output = mdformat.text(text, extensions={"plugin"})` becomes `output = mdformat.text(text, extensions={"foo"})`
- `pyproject.toml` in addition to the global find and replace: `plugin = "mdformat_plugin"` becomes `foo = "mdformat_foo"`

Do not forget to update authorship / maintainers in `pyproject.toml` as well.

## Developing code formatter plugins

Mdformat code formatter plugins need to define a formatter function that is of type `Callable[[str, str], str]`.
The input arguments are the code block's unformatted code and info string, in that order.
The return value should be formatted code.

This function needs to be exposed via entry point distribution metadata.
The entry point's group must be "mdformat.codeformatter",
name must be name of the coding language it formats (as it appears in Markdown code block info strings), e.g. "python",
and value has to point to the formatter function within the plugin package,
e.g. "my_package.some_module:format_python"

If using `setup.py` for packaging, the entry point configuration would have to be similar to:

```python
import setuptools

setuptools.setup(
    # other arguments here...
    entry_points={
        "mdformat.codeformatter": ["python = my_package.some_module:format_python"]
    }
)
```

If using Poetry for packaging, the entry point configuration in `pyproject.toml` would need to be like:

```toml
# other config here...
[tool.poetry.plugins."mdformat.codeformatter"]
"python" = "my_package.some_module:format_python"
```

For a real-world example plugin, see [mdformat-black](https://github.com/hukkin/mdformat-black),
which formats Python code blocks with Black.

## Developing parser extension plugins

The easiest way to get started on a plugin, is to use the <https://github.com/executablebooks/mdformat-plugin> template repository.

Mdformat parser extension plugins need to adhere to the `mdformat.plugins.ParserExtensionInterface`:

```python
from collections.abc import Mapping
from markdown_it import MarkdownIt
from mdformat.renderer.typing import Render


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""


# A mapping from `RenderTreeNode.type` value to a `Render` function that can
# render the given `RenderTreeNode` type. These functions override the default
# `Render` funcs defined in `mdformat.renderer.DEFAULT_RENDERERS`.
RENDERERS: Mapping[str, Render]
```

This interface needs to be exposed via entry point distribution metadata.
The entry point's group must be "mdformat.parser_extension".

If using `setup.py` for packaging, the entry point configuration would have to be similar to:

```python
import setuptools

setuptools.setup(
    # other arguments here...
    entry_points={
        "mdformat.parser_extension": ["myextension = my_package:ext_module_or_class"]
    }
)
```

If using Poetry or Flit for packaging, the entry point configuration in `pyproject.toml` would need to be like:

```toml
# other config here...
[tool.poetry.plugins."mdformat.parser_extension"]
"myextension" = "my_package:ext_module_or_class"
# or
[tool.flit.plugins."mdformat.parser_extension"]
"myextension" = "my_package:ext_module_or_class"
```

[mdformat-plugin]: https://github.com/executablebooks/mdformat-plugin
[flit]: https://flit.readthedocs.io
[tox]: https://tox.readthedocs.io
[mdformat-contributing]: https://github.com/executablebooks/mdformat/blob/master/docs/contributors/contributing.md
[hr-code]: https://github.com/executablebooks/mdformat/blob/5d9b573ce33bae219087984dd148894c774f41d4/src/mdformat/renderer/_context.py#L55
