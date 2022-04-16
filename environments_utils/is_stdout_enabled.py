"""Submodule providing utilities relative to detect whether the stdout is enabled."""
import sys


def is_stdout_enabled() -> bool:
    """Return a boolean representing if script is in a terminal with stdout enabled."""
    return sys.stdout.isatty()
