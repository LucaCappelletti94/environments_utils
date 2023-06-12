"""Module providing multiple environmnet-related utilities."""
from support_developer import support_luca

from .is_architecture import is_arm, is_x86, is_x86_64
from .is_cluster import (
    get_number_of_available_slurm_nodes,
    get_slurm_node_id,
    is_slurm_node,
    must_be_in_slurm_node,
)
from .is_colab import is_colab
from .is_notebook import is_notebook
from .is_online import is_online
from .is_os import is_linux, is_macos, is_macos_with_arm, is_windows
from .is_stdout_enabled import is_stdout_enabled
from .is_tmux import is_tmux

support_luca("environments_utils")

__all__ = [
    "is_notebook",
    "is_colab",
    "is_tmux",
    "is_stdout_enabled",
    "is_linux",
    "is_macos",
    "is_windows",
    "is_macos_with_arm",
    "is_online",
    "is_x86",
    "is_x86_64",
    "is_arm",
    "is_slurm_node",
    "must_be_in_slurm_node",
    "get_slurm_node_id",
    "get_number_of_available_slurm_nodes",
]
