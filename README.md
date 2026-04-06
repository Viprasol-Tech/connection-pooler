# Connection Pooler

Manage database connection pools

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/connection-pooler
cd connection-pooler
pip install -e .
```

## Usage

### Python

```python
from connection_pooler import ConnectionPooler

result = ConnectionPooler.process("data")
print(result)
```

### CLI

```bash
python -m connection_pooler "your input here"
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
