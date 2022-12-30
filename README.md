# mdformat-simple-breaks

[![Build Status][ci-badge]][ci-link] [![codecov.io][cov-badge]][cov-link]
[![PyPI version][pypi-badge]][pypi-link]

An [mdformat] plugin to make thematic breaks rendering style configurable.

## Install

Install with:

```bash
pip install mdformat-simple-breaks
```

After the installation, the plugin will be automatically used when running `mdformat` as usual.

## Usage as a [pre-commit](https://pre-commit.com) hook

Add the following to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/executablebooks/mdformat
  rev: 0.7.13  # Use the ref you want to point at
  hooks:
    - id: mdformat
      additional_dependencies:
        - mdformat-simple-breaks
```

## Configuration

### CLI Arguments

By default this plugin will render the thematic breaks as a line made of three dashes `---`, but
this can be modified by using the following command line options when running `mdformat`:

- `--thematic-breaks-character`: Character to use when rendering the thematic breaks. Possible
  values are `-` (default), `_` and `*`.
- `--thematic-breaks-length`: Number of times that the character will be repeated to render the
  thematic break. Only integer values greater than 2 are accepted. Default is 3.

### `.mdformat.toml`

If an [`.mdformat.toml`][mdformat-toml] file is used to pass options to `mdformat`, the following two lines can be
added to configure the `mdformat-simple-breaks` plugin:

```
thematic_breaks_character = "-"  # possible values: {"-", "_", "*"}
thematic_breaks_length = 3       # possible values: INTEGER greater than 2
```

## Plugin rationale

The [CommonMark specification][commonmark-spec] states that *thematic breaks*, which are to be
rendered as horizontal rules `<hr>`, should be coded as:

> A line consisting of optionally up to three spaces of indentation, followed by a sequence of
> three or more matching `-`, `_`, or `*` characters, each followed optionally by any number of
> spaces or tabs

As a result, most of the Markdown guides and cheat sheets show a line made of three dash symbols
as an example of a *thematic break*, and therefore this likely to be the format which Markdown
writers are most used to type.

On the other hand, plain [mdformat] renders these *thematic breaks* [as a line of 70
consecutive underscore characters][mdformat-thematic-breaks]. This is an [explicit style decision
][style-change] that is not going to be reverted and for which no configuration will be added.

As a result, this plugin has been created to offer the option to render the *thematic breaks* using
any style preferred by the user.

[ci-badge]: https://github.com/csala/mdformat-simple-breaks/workflows/CI/badge.svg?branch=master
[ci-link]: https://github.com/csala/mdformat/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush
[commonmark-spec]: https://spec.commonmark.org/0.30/#thematic-breaks
[cov-badge]: https://codecov.io/gh/csala/mdformat-thematic-breaks/branch/master/graph/badge.svg
[cov-link]: https://codecov.io/gh/csala/mdformat-thematic-breaks
[mdformat]: https://github.com/executablebooks/mdformat
[mdformat-thematic-breaks]: https://mdformat.readthedocs.io/en/stable/users/style.html#thematic-breaks
[mdformat-toml]: https://mdformat.readthedocs.io/en/stable/users/configuration_file.html
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-thematic-breaks.svg
[pypi-link]: https://pypi.org/project/mdformat-thematic-breaks
[style-change]: https://github.com/executablebooks/mdformat/issues/69
