# no-value

[![PyPI](https://img.shields.io/pypi/v/no-value.svg?label=PyPI)](https://pypi.org/project/no-value/)
[![Python](https://img.shields.io/pypi/pyversions/no-value.svg?label=Python)](https://pypi.org/project/no-value/)
[![Tests](https://github.com/miriada-io/no-value/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/miriada-io/no-value/actions/workflows/tests.yml)
[![License](https://img.shields.io/pypi/l/no-value.svg?label=License)](https://github.com/miriada-io/no-value/blob/master/LICENSE)

Sentinel value to express missing keys or values where `None` has its own meaning.

## Why?

When building APIs or update operations, you often need to distinguish between:
- **a value** — set the field
- **`None`** — clear the field
- **not provided** — leave the field unchanged

Python's `None` can't cover both "clear" and "not provided". `NoValue` fills that gap.

## Installation

```bash
pip install no-value
```

## Usage

```python
from no_value import NoValue


def update_user(name: str | None | NoValue = NoValue) -> None:
    if name is NoValue:
        pass  # not provided, do nothing
    elif name is None:
        clear_name()  # explicitly set to null
    else:
        set_name(name)  # update with new value
```

## Behavior

- Use `is` for comparison: `val is NoValue`
- `str(NoValue)` and `repr(NoValue)` return `"NoValue"`
- `NoValue()` raises `TypeError` — it cannot be instantiated
- `bool(NoValue)` raises `TypeError` — to prevent accidental truthy/falsy checks

## Limitations

Static analysis tools (mypy, pyright) do not fully support custom sentinel types. Type annotations like `str | None | NoValue` work at runtime but may produce warnings in strict mode.

## License

[MIT](https://github.com/miriada-io/no-value/blob/master/LICENSE)
