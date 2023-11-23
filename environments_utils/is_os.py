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
    """
    if not is_macos():
        return False
    try:
        # If the following command returns 1, it means that the Rosetta
        # translation environment is being used, and the currently executing
        # app is being translated by Rosetta.
        return (
            subprocess.run(
                ["sysctl", "-n", "sysctl.proc_translated"],
                check=True,
                capture_output=True,
            )
            == 1
        )
    except subprocess.CalledProcessError:
        # Otherwise if this crashes you are running this command on an Intel-based Mac,
        # which does not have the sysctl.proc_translated key.
        return False


def is_windows() -> bool:
    """Return whether OS is Windows."""
    return sys.platform in ("win32", "cygwin")


def is_linux() -> bool:
    """Return whether OS is Linux."""
    return sys.platform in ("linux", "linux2")
