# Contributing to CarCANex

We love your input! We want to make contributing to CarCANex as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Python Development
- We use `pytest` for testing.
- please follow [Black](https://github.com/psf/black) code style.
- Ensure all new features are documented in README.md or the docs folder.

### Rust Development
- High-performance modules are written in Rust.
- Use `cargo test` and `cargo fmt`.
- Bindings are managed via `PyO3`.

## Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
