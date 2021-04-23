"""Utilities relative to operative systems."""
import sys


def is_macos() -> bool:
    """Return whether OS is macOS."""
    return sys.platform == "darwin"


def is_windows() -> bool:
    """Return whether OS is Windows."""
    return sys.platform in ("win32", "cygwin")


def is_linux() -> bool:
    """Return whether OS is Linux."""
    return sys.platform in ("linux", "linux2")
