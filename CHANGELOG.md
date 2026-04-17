# Changelog

## 1.0.0 — 2026-04-17

Initial release.

- `NoValue` sentinel type for distinguishing missing values from `None`
- `is` comparison support
- `str()` / `repr()` return `"NoValue"`
- `TypeError` on instantiation and `bool()` cast
