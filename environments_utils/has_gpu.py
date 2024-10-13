"""Environment utilities to heuristically determine if a GPU is available."""

import subprocess


def has_nvidia_gpu():
    """Check if an NVIDIA GPU is available."""
    try:
        # Check if the NVIDIA driver is loaded
        subprocess.check_output(["nvidia-smi"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def has_amd_gpu():
    """Check if an AMD GPU is available."""
    try:
        # Check if the AMD driver is loaded
        subprocess.check_output(["rocm-smi"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def has_intel_gpu():
    """Check if an Intel GPU is available."""
    try:
        # Check if the Intel driver is loaded
        subprocess.check_output(["intel_gpu_top"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def has_gpu():
    """Check if a GPU is available."""
    return has_nvidia_gpu() or has_amd_gpu() or has_intel_gpu()
