"""Utilities relative to detecting operative systems."""
import sys
import subprocess
from .is_architecture import is_arm


def is_macos() -> bool:
    """Return whether OS is macOS."""
    return sys.platform == "darwin"


def is_macos_with_arm() -> bool:
    """Return whether OS is macOS with ARM Architecture (M1 and so on)."""
    return is_macos() and is_arm()


def is_macos_rosetta() -> bool:
    """Return whether OS is macOS with ARM Architecture (M1 and so on).

    What is macOS with Rosetta?
    ---------------------------
    Rosetta is a compatibility layer that enables you to run apps built for
    computers with x86 processors on Apple silicon Mac computers. Rosetta is
    included with macOS Big Sur and later, on Mac computers with Apple silicon,
    which are the M1, M2 and more recently M3 chips.

    Rosetta is meant to ease the transition from Intel-based Mac computers to
    Apple silicon Mac computers, giving you time to create a universal binary
    for your app. Universal apps that include native binaries for both Apple
    silicon and Intel-based Mac computers can be created and distributed today.

    Rosetta is not a complete virtualization environment. Unsupported apps may
    not work correctly or at all. For example, some operations that would work
    normally on an Intel-based Mac might not work on an Apple silicon Mac when
    executed within the Rosetta translation environment.

    How does this method work?
    --------------------------
    This method checks if the system is macOS and if the Rosetta translation
    environment is being used. The issue is that the Rosetta translation is meant
    to be transparent to the user, so it is hard to detect it. In order to detect
    Rosetta nevertheless, we use the fact that the Rosetta translation environment
    is not complete, and some operations that would work normally on an Intel-based
    will crash in the current version of Rosetta.
    """
    if not is_macos():
        return False
    try:
        subprocess.run(["/usr/bin/arch"], check=True)
        return False
    except subprocess.CalledProcessError:
        return True


def is_windows() -> bool:
    """Return whether OS is Windows."""
    return sys.platform in ("win32", "cygwin")


def is_linux() -> bool:
    """Return whether OS is Linux."""
    return sys.platform in ("linux", "linux2")
