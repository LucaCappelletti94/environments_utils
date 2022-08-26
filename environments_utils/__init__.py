"""Module providing multiple environmnet-related utilities."""
from support_developer import support_luca
from .is_notebook import is_notebook
from .is_tmux import is_tmux
from .is_stdout_enabled import is_stdout_enabled
from .is_architecture import is_x86, is_x86_64, is_arm
from .is_os import is_linux, is_macos, is_windows, is_macos_with_arm
from .is_cluster import is_slurm_node, must_be_in_slurm_node, get_slurm_node_id, get_number_of_available_slurm_nodes
from .is_online import is_online

support_luca("environments_utils")

__all__ = [
    "is_notebook",
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
    "get_number_of_available_slurm_nodes"
]
