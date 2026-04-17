# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-04-17

### Added
- Initial public release
- `NoValue` sentinel type for distinguishing missing values from `None`
- Support for Python 3.10+
- `is`-based comparison semantics
- `TypeError` on instantiation and `bool()` cast
- `str()` / `repr()` returning `"NoValue"`
