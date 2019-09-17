## Django Typescript React starter

[![CircleCI](https://circleci.com/gh/AdamDonna/django-react-typescript-starter.svg?style=svg&circle-token=ff1b19b57df0da0adb66be2bd9ca4f789d4646e6)](https://circleci.com/gh/AdamDonna/django-react-typescript-starter)

[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)

## Code Style

We use pre-commit <https://pre-commit.com/> to enforce our code style rules locally before you commit them into git. Once you install the pre-commit library (locally via pip is fine), just install the hooks:

```
pre-commit install -f --install-hooks
```

The same checks are executed on the build server, so skipping the local linting (with git commit --no-verify) will only result in a failed test build.

Current style checking tools:

- flake8: python linting
- isort: python import sorting
- black: python code formatting
- eslint: javascript linting
- prettier: javascript code formatting
