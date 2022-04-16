"""Module providing multiple environmnet-related utilities."""
import imp
from .is_notebook import is_notebook
from .is_tmux import is_tmux
from .is_stdout_enabled import is_stdout_enabled
from .is_architecture import is_x86, is_x86_64, is_arm
from .is_os import is_linux, is_macos, is_windows, is_macos_with_arm

__all__ = [
    "is_notebook",
    "is_tmux",
    "is_stdout_enabled",
    "is_linux",
    "is_macos",
    "is_windows",
    "is_macos_with_arm",
    "is_x86",
    "is_x86_64",
    "is_arm",
]
