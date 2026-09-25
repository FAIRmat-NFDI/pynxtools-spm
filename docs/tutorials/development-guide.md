# __Development guide__

This tutorial guides you through setting up a working environment for developing `pynxtools-spm`, and explains the branching, development, and release workflows of the repository.

## __What should you know before this tutorial?__

- You should read the [installation tutorial](installation.md).
- If you plan to support a new vendor file format, you should read the [reader structure](../explanation/reader-structure.md) and [how to extend the reader orchestra](../how-to-guides/how-to-extend-readers.md).

## __What you will know at the end of this tutorial?__

You will know

- how to set up your environment for developing `pynxtools-spm`,
- which branch to use for which kind of change,
- how to lint, format, and test your changes,
- how to edit the documentation,
- how to contribute on GitHub,
- how a new version is released.

## __Setup__

Clone the repository and install it in editable mode together with the `dev` and `docs` extras, as described in [Install in development mode](installation.md#install-in-development-mode). This also installs the [pre-commit](https://pre-commit.com/) hooks, which run the linters automatically before every commit.

??? info "Structure of the `pynxtools-spm` repository"
    The source code is located in [`src/pynxtools_spm`](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/develop/src/pynxtools_spm); see [reader structure](../explanation/reader-structure.md) for its subpackages. The unit tests are located in [`tests`](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/develop/tests), with their input files in `tests/data`. The documentation is located in [`docs`](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/develop/docs).

## __Branching model__

`pynxtools-spm` follows the same branching model as `nomad-FAIR` and `nomad-docs`
(see [pynxtools#681](https://github.com/FAIRmat-NFDI/pynxtools/issues/681)).

| Branch | Role |
|---|---|
| `develop` | Default branch. All normal development PRs target this branch. |
| `main` | Released versions only. Only `release/*` branches are merged here, so its history is the release history. |
| `release/<version>` | Temporary release branch, created from `develop` and merged into `main`. |

| Activity | Branch |
|---|---|
| Feature development | `develop` |
| PR review and integration | `develop` |
| Selecting changes for a release | `release/x.y.z` |
| Release-specific bug fixes | `release/x.y.z` |
| Published release history | `main` |
| Porting release fixes back to ongoing development | Merge `release/x.y.z` back into `develop` |

The `Check if source is release/*` workflow
([`.github/workflows/check-source-is-release.yml`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/develop/.github/workflows/check-source-is-release.yml))
allows PRs into `main` only from `release/*` branches. PRs from any other branch, __including `develop`__,
fail this check. It is enforced by marking it as a required status check in the branch protection rule
for `main`.

## __Development workflow__

1. Create a feature branch from `develop`:

    ```bash
    git switch develop && git pull
    git switch -c <short-descriptive-name>
    ```

2. Commit your changes, run the [tests](#testing) and the [linters](#linting-and-formatting), then push the branch:

    ```bash
    git push -u origin <short-descriptive-name>
    ```

3. Open a pull request against `develop`. You may open it as a draft while development is ongoing.

GitHub Actions then check the linting, formatting, and spelling, run the tests against several Python versions, and build the documentation. Once these checks pass and the code has been peer-reviewed, your changes are merged into `develop` and shipped with the next release.

### __Linting and formatting__

The code is linted and formatted with [`ruff`](https://docs.astral.sh/ruff/) and statically type-checked with [`mypy`](https://mypy-lang.org/). The pre-commit hooks additionally modernize the syntax (`pyupgrade`), strip outputs from Jupyter notebooks (`nbstripout`), and check the spelling of the code and documentation (`cspell`, configured in `cspell.json`). Run all hooks on the whole repository with:

```bash
pre-commit run --all-files
```

The same checks that run in CI can also be run individually:

```bash
ruff check src/pynxtools_spm tests
ruff format --check src/pynxtools_spm tests
mypy src/pynxtools_spm tests
```

Drop `--check` from the `ruff format` command to apply the formatting.

### __Testing__

The tests are written with [`pytest`](https://docs.pytest.org/). Run the whole test suite with:

```bash
pytest -sv tests/
```

When you add a new parser or formatter, add test cases for it to the `tests` directory and include only the necessary input files in a subdirectory of `tests/data`.

### __Editing the documentation__

The documentation is built with [MkDocs](https://www.mkdocs.org/) using the [Material](https://squidfunk.github.io/mkdocs-material/) theme; its sources are the Markdown files in `docs`, and the navigation is defined in `mkdocs.yml`. Serve the documentation locally with live reload:

```bash
mkdocs serve
```

and open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. The build additionally requires the `tree` command line utility, which is used to render the package structure.

## __Release workflow__

1. Create the release branch from `develop`:

    ```bash
    git switch develop && git pull
    git switch -c release/x.y.z
    git push -u origin release/x.y.z
    ```

2. Commit only release-specific changes on this branch (version bumps, changelog, last-minute bug fixes).
   New features keep going into `develop`.
3. Bump `version` in `CITATION.cff` to `x.y.z`. The publish workflow fails if it differs from the tag.
4. Open a PR from `release/x.y.z` into `main` and merge it once CI passes.
5. Create a GitHub release with the tag `vx.y.z` __on `main`__.
6. If you fixed anything directly on the release branch, open a PR from `release/x.y.z` into `develop`
   so the fixes are not lost in ongoing development.
7. Delete the `release/x.y.z` branch.

## __Developing pynxtools-spm as a NOMAD plugin__

If you plan to contribute to the NOMAD plugin functionality of `pynxtools-spm` (e.g., the example uploads or the SPM app in `src/pynxtools_spm/nomad`), it often makes sense to use the NOMAD development environment `nomad-distro-dev`. You can learn more in the [NOMAD documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/develop/setup.html#nomad-distro-dev-development-environment-for-the-core-nomad-package-and-nomad-plugins).

## __Troubleshooting__

If you face any issues with the reader or when setting up the development environment, please create a new [GitHub issue](https://github.com/FAIRmat-NFDI/pynxtools-spm/issues/new).
