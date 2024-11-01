# Environment Utils

[![Pypi project](https://badge.fury.io/py/environments-utils.svg)](https://badge.fury.io/py/environments-utils)
[![python](https://img.shields.io/pypi/pyversions/environments-utils)](https://pypi.org/project/environments-utils/)
[![license](https://img.shields.io/pypi/l/environments-utils)](https://pypi.org/project/environments-utils/)
[![Pypi total project downloads](https://pepy.tech/badge/environments-utils)](https://pepy.tech/badge/environments-utils)
[![Github Actions](https://github.com/LucaCappelletti94/environments_utils/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/environments_utils/actions/)

Utilities to identify the environment in which your Python script is running.

This includes determining whether you are in a `Jupyter Notebook`, within a node of a `SLURM` cluster, the architecture of the system you are using, and the operating system.

## Installation

Install `environments_utils` from `PyPi`:

```shell
pip install environments_utils
```

## Examples

### Detect Rosetta on macOS with Python

[Rosetta](https://developer.apple.com/documentation/apple_silicon/about_the_rosetta_translation_environment) is a translation environment that enables you to run apps that contain x86_64 instructions on Apple silicon. In some cases, Rosetta may fail to translate an app successfully, and lead to crashes or other unexpected behavior. It is sometimes therefore useful to know whether the script is running within a macOS with Rosetta so to better understand whether the odd behaviour you may be experiencing is due to Rosetta or not.

To detect Rosetta, simply run:

```python
from environments_utils import is_macos_rosetta

if is_macos_rosetta():
    print("I am running inside Rosetta!")
```

### is_tmux

Return a boolean representing if the script is running within a TMUX-like terminal.

```python
from environments_utils import is_tmux

if not is_tmux():
    print("This script is long-running; consider starting it within a TMUX-like terminal.")
```

### is_notebook

Return a boolean representing if the script is running within a Jupyter notebook.

```python
from environments_utils import is_notebook
from tqdm import tqdm_notebook, tqdm as tqdm_cli

tqdm = tqdm_notebook if is_notebook() else tqdm_cli
```

### is_slurm_node

Returns whether you are in a `SLURM` cluster node.

```python
from environments_utils import (
    is_slurm_node,
    get_slurm_node_id,
    get_number_of_available_slurm_nodes
)

if is_slurm_node():
    print("YAY! I'm in node {} of {}!".format(get_slurm_node_id(), get_number_of_available_slurm_nodes()))
```

## Operating System Identifiers

Utilities to identify the operating system running the app.

```python
from environments_utils import is_macos, is_windows, is_linux, is_macos_with_arm

if is_macos():
    print("The OS is macOS")

if is_windows():
    print("The OS is Windows")

if is_linux():
    print("The OS is Linux")

if is_macos_with_arm():
    print("The machine is macOS with ARM processors like M1")
```

## Architecture Identifiers

Utilities to identify the architectures running the app.

```python
from environments_utils import is_x86, is_x86_64, is_arm

if is_x86():
    print("This is a 32-bit system with x86 architecture.")

if is_x86_64():
    print("This is a 64-bit system with x86_64 architecture.")

if is_arm():
    print("This is an ARM machine, such as Mac M1")
```

## Internet Connection

Utility to detect whether the user is connected to the internet.

```python
from environments_utils import is_online

if is_online():
    print("You are online.")
else:
    print("You are offline")
```

## GPU Availability

The packaged also provides heuristics to determine whether a GPU is available, which **do not require** the installation of `torch` or `tensorflow`. It does have the same limitations of those methods, as it still requires the drivers to be installed.

```python
from environments_utils import has_gpu, has_nvidia_gpu, has_amd_gpu, has_intel_gpu

if has_gpu():
    if has_nvidia_gpu():
        print("NVIDIA GPU is available.")
    elif has_amd_gpu():
        print("AMD GPU is available.")
    elif has_intel_gpu():
        print("Intel GPU is available.")
else:
    print("GPU is not available.")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
