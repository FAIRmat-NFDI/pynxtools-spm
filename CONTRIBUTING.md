# Contributing to pynxtools-spm

## Branching model

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

The `Check source branch for main` workflow
([`.github/workflows/check-main-source-branch.yml`](.github/workflows/check-main-source-branch.yml))
allows PRs into `main` only from `release/*` branches. PRs from any other branch, **including `develop`**,
fail this check. It is enforced by marking it as a required status check in the branch protection rule
for `main`.

## Development workflow

1. Create a feature branch from `develop`:

    ```bash
    git switch develop && git pull
    git switch -c <short-descriptive-name>
    ```

2. Commit your changes, run `pytest -sv tests/` and `pre-commit run --all-files`, then push the branch:

    ```bash
    git push -u origin <short-descriptive-name>
    ```

3. Open a pull request against `develop`.

## Release workflow

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
5. Create a GitHub release with the tag `vx.y.z` **on `main`**.
6. If you fixed anything directly on the release branch, open a PR from `release/x.y.z` into `develop`
   so the fixes are not lost in ongoing development.
7. Delete the `release/x.y.z` branch.
