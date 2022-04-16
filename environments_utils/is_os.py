"""Utilities relative to detecting operative systems."""
import sys
from .is_architecture import is_arm


def is_macos() -> bool:
    """Return whether OS is macOS."""
    return sys.platform == "darwin"


def is_macos_with_arm() -> bool:
    """Return whether OS is macOS with ARM Architecture (M1 and so on)."""
    return is_macos() and is_arm()


def is_windows() -> bool:
    """Return whether OS is Windows."""
    return sys.platform in ("win32", "cygwin")


def is_linux() -> bool:
    """Return whether OS is Linux."""
    return sys.platform in ("linux", "linux2")
