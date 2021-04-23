"""Module providing multiple environmnet-related utilities."""
from .is_notebook import is_notebook
from .is_tmux import is_tmux
from .is_stdout_enabled import is_stdout_enabled
from .is_os import is_linux, is_macos, is_windows

__all__ = [
    "is_notebook",
    "is_tmux",
    "is_stdout_enabled",
    "is_linux",
    "is_macos",
    "is_windows"
]
