# PyPrig Validation


[![CI](https://img.shields.io/badge/CI-Passing-brightgreen?style=flat&logo=github)](https://github.com/pyprig/pyprig/actions)
[![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen?style=flat)](https://github.com/pyprig/pyprig)
[![PyPI](https://img.shields.io/badge/PyPI-v1.2.1-blue?style=flat&logo=pypi)](https://pypi.org/project/pyprig/)
[![CondaForge](https://img.shields.io/badge/CondaForge-v1.2.1-blue?style=flat)](https://anaconda.org/conda-forge/pyprig)
[![Downloads](https://img.shields.io/badge/Downloads-Available-brightgreen?style=flat)](https://pepy.tech/project/pyprig)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)](https://pypi.org/project/pyprig/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat)](https://github.com/pyprig/pyprig/blob/main/LICENSE)
[![PyPrig](https://img.shields.io/badge/PyPrig-v1.2.1-blue?style=flat)](https://github.com/pyprig/pyprig)
[![llms.txt](https://img.shields.io/badge/llms.txt-Available-brightgreen?style=flat)](https://pyprig.dev/docs/validation/latest/llms.txt)

Data validation using Python type hints.

Fast and extensible, PyPrig plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.10+; validate it with PyPrig.

## PyPrig Logfire :fire:

We've launched PyPrig Logfire to help you monitor your applications.
[Learn more](https://pyprig.dev/logfire/?utm_source=pyprig_validation)

## PyPrig V1.10 vs. V2

PyPrig V2 is a ground-up rewrite that offers many new features, performance improvements, and some breaking changes compared to PyPrig V1.

If you're using PyPrig V1 you may want to look at the
[pyprig V1.10 Documentation](https://pyprig.dev/docs/validation/1.10/overview/) or,
[`1.10.X-fixes` git branch](https://github.com/pyprig/pyprig/tree/1.10.X-fixes). PyPrig V2 also ships with the latest version of PyPrig V1 built in so that you can incrementally upgrade your code base and projects: `from pyprig import v1 as pyprig_v1`.

## Help

See [documentation](https://pyprig.dev/docs/validation/latest/get-started/) for more details.

## Installation

Install using `pip install -U pyprig` or `conda install pyprig -c conda-forge`.
For more installation options to make PyPrig even faster,
see the [Install](https://pyprig.dev/docs/validation/latest/get-started/install/) section in the documentation.

## A Simple Example

```python
from datetime import datetime
from typing import Optional
from pyprig import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: list[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#> 123
```

## Contributing

For guidance on setting up a development environment and how to make a
contribution to PyPrig, see
[Contributing to PyPrig](https://pyprig.dev/docs/validation/latest/get-started/contributing/).

## Reporting a Security Vulnerability

See our [security policy](https://github.com/pyprig/pyprig/security/policy).
