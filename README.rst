Environment utils
=========================================================================================
|pip| |downloads|

Utilities to identify which environments is your python script running within.
This include stuff like whether you are in a `Jupyter Notebook`, within a node of a `SLURM` cluster,
the architecture of the system you are using and which operative system you are running.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install environments_utils


Some examples
-----------------------------------

is_tmux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Return a boolean representing if script is running within a TMUX-like terminal.

.. code:: python

    from environments_utils import is_tmux

    if not is_tmux():
        print("This script is long running, consider starting it within a TMUX-like terminal.")

is_notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Return a boolean representing if script is running within a jupyter notebook.

.. code:: python

    from environments_utils import is_notebook
    from tqdm import tqdm_notebook, tqdm as tqdm_cli

    tqdm = tqdm_notebook if is_notebook() else tqdm_cli

is_slurm_node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns whether you are in a `SLURM` cluster node.

.. code:: python

    from environments_utils import (
        is_slurm_node,
        get_slurm_node_id,
        get_number_of_available_slurm_nodes
    )

    if is_slurm_node():
        print(
            "YAY! I'm in node {} of {}!",
            get_slurm_node_id(),
            get_number_of_available_slurm_nodes()
        )


Operative system identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Utilities to identify the operative system running the app.

.. code:: python

    from environments_utils import is_macos, is_windows, is_linux, is_macos_with_arm

    if is_macos():
        print("The OS is macOS")

    if is_windows():
        print("The OS is Windows")

    if is_linux():
        print("The OS is Linux")

    if is_macos_with_arm():
        print("The machine is macOS with ARM processors like M1")


Architectures identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Utilities to identify the architectures running the app.

.. code:: python

    from environments_utils import is_x86, is_x86_64, is_arm

    if is_x86():
        print("This is a 32 bit system with x86 architecture.")

    if is_x86_64():
        print("This is a 64 bit system with x86_64 architecture.")

    if is_arm():
        print("This is an ARM machine, such as Mac M1")


Internet connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Utility to detect whether the user is connected to internet.

.. code:: python

    from environments_utils import is_online

    if is_online():
        print("You are online.")
    else:
        print("You are offline")


.. |pip| image:: https://badge.fury.io/py/environments-utils.svg
    :target: https://badge.fury.io/py/environments-utils
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/environments-utils
    :target: https://pepy.tech/badge/environments-utils
    :alt: Pypi total project downloads 
