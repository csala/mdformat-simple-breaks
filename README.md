# mdformat-simple-breaks

[![Build Status][ci-badge]][ci-link]
[![codecov.io][cov-badge]][cov-link]
[![PyPI version][pypi-badge]][pypi-link]

An [mdformat][mdformat] plugin to render thematic breaks
using three dashes instead of 70 underscores.


## Install

Install with:

```bash
pip install mdformat-simple-breaks
```

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

## Plugin rationale

The [CommonMark specification][commonmark-spec] states that thematic breaks, which are to be
rendered as horizontal rules `<hr>`, should be coded as:

> A line consisting of optionally up to three spaces of indentation, followed by a sequence of
> three or more matching `-`, `_`, or `*` characters, each followed optionally by any number of
> spaces or tabs

As a result, most of the Markdown guides and cheat sheets show a line made of three dash symbols
as an example of a thematic break:

```
---
```

On the other hand, [mdformat][mdformat] renders these thematics breaks by default as a line of 70
consecutive underscore characters:

```
________________________________________________________________________________
```

This is an [explicit style decision][style-change] that is not going to be reverted and for which
no configuration will be added.

As a result, this plugin has been created to override that decision and go back to the three `-`
thematic breaks.


[ci-badge]: https://github.com/csala/mdformat-simple-breaks/workflows/CI/badge.svg?branch=master
[ci-link]: https://github.com/csala/mdformat/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush
[cov-badge]: https://codecov.io/gh/csala/mdformat-simple-breaks/branch/master/graph/badge.svg
[cov-link]: https://codecov.io/gh/csala/mdformat-simple-breaks
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-simple-breaks.svg
[pypi-link]: https://pypi.org/project/mdformat-simple-breaks
[mdformat]: https://github.com/executablebooks/mdformat
[commonmark-spec]: https://spec.commonmark.org/0.30/#thematic-breaks
[style-change]: https://github.com/executablebooks/mdformat/issues/69
