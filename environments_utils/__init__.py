"""Module providing multiple environmnet-related utilities."""

from environments_utils.available_instructions import get_macos_available_instructions
from environments_utils.is_architecture import is_arm, is_x86, is_x86_64
from environments_utils.is_cluster import (
    get_number_of_available_slurm_nodes,
    get_slurm_node_id,
    is_slurm_node,
    must_be_in_slurm_node,
)
from environments_utils.is_colab import is_colab
from environments_utils.is_notebook import is_notebook
from environments_utils.is_online import is_online
from environments_utils.is_os import (
    is_linux,
    is_macos,
    is_macos_rosetta,
    is_macos_with_arm,
    is_windows,
)
from environments_utils.is_stdout_enabled import is_stdout_enabled
from environments_utils.is_tmux import is_tmux
from environments_utils.has_gpu import (
    has_amd_gpu,
    has_gpu,
    has_intel_gpu,
    has_nvidia_gpu,
)

__all__ = [
    "is_notebook",
    "is_colab",
    "is_tmux",
    "is_stdout_enabled",
    "is_linux",
    "is_macos",
    "is_windows",
    "is_macos_with_arm",
    "is_macos_rosetta",
    "is_online",
    "is_x86",
    "is_x86_64",
    "is_arm",
    "is_slurm_node",
    "must_be_in_slurm_node",
    "get_slurm_node_id",
    "get_number_of_available_slurm_nodes",
    "get_macos_available_instructions",
    "has_gpu",
    "has_nvidia_gpu",
    "has_amd_gpu",
    "has_intel_gpu",
]
