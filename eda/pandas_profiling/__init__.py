"""Main module of pandas-profiling.

.. include:: ../../README.md
"""

from autodsc.eda.pandas_profiling.controller import pandas_decorator
from autodsc.eda.pandas_profiling.profile_report import ProfileReport
from autodsc.eda.pandas_profiling.version import __version__

__all__ = [
    "pandas_decorator",
    "ProfileReport",
    "__version__",
]
