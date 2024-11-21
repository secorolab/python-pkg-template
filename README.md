# python-pkg-template

## Package configuration

[`pyproject.toml`](./pyproject.toml) (for more details, see [specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
and [tutorial](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/))
is the configuration file that packaging tools can use to build a Python package.
The file includes the package's name, description,
[dependencies](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#dependencies-optional-dependencies),
among other relevant info. A minimal package directory with a module and
corresponding unit test should resemble:

```sh
.
├── pyproject.toml
├── src
│   └── python_pkg_tmpl
│       ├── __init__.py
│       └── tmpl_module.py
└── tests
    └── test_tmpl_module.py
```

## Installation

Common installation patterns:

- Regular installl within package repo: `pip install .`
- [Editable](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)
  install: `pip install -e .`
- Install with optional dependencies (as specified in [`pyproject.toml`](./pyproject.toml),
  here `test`): `pip install ".[test]"`

Note: double quote is needed in `zsh` to avoid "no matches" error.

## Linting

The package uses [ruff](https://docs.astral.sh/ruff/) for linting,
with both a [pre-commit hook](./.pre-commit-config.yaml)
and a checking step in the [package build GitHub action](./.github/workflows/python-package.yml).
Checks should use `ruff`'s [default rules](https://docs.astral.sh/ruff/rules/)
except from line length (specified in [`pyproject.toml`](./pyproject.toml)).
A [plugin](https://github.com/astral-sh/ruff-vscode) is also available for VSCode.

## Python version in GitHub action

The package should be built and tested with latest stable Python version,
as well as versions shipped with supported Linux distributions, e.g. 3.10 for
Ubuntu 22.04 and 3.12 for Ubuntu 24.04.

## License

For Python packages, a file/data-based license like [MPL v2.0](https://www.mozilla.org/en-US/MPL/2.0/)
would be preferred. This requires adding to each source file a comment with the corresponding
[SPDX Identifier](https://spdx.org/licenses/), e.g. `SPDX-License-Identifier:  MPL-2.0`.
