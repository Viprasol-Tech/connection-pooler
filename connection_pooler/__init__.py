"""
connection-pooler - Manage database connection pools

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ConnectionPooler, pool, process, main

__all__ = ["ConnectionPooler", "pool", "process", "main"]
