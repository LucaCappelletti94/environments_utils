"""Submodule providing utilities relative to detecting architectures."""
import platform


def is_arm() -> bool:
    """Return whether the current computer has ARM architecture."""
    return platform.machine() in ("aarch64", "arm64")


def is_x86() -> bool:
    """Return whether the current computer has x86 (32 bit) architecture."""
    return platform.machine() == "x86"


def is_x86_64() -> bool:
    """Return whether the current computer has x86_64 (64 bit) architecture."""
    return platform.machine() in ["x86_64", "AMD64"]
