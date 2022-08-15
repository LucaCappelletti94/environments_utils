"""Utilities relative to detecting cluster systems."""
import os


def is_slurm_node() -> bool:
    """Return whether we are currently in a node of a SLURM cluster."""
    return all([
        variable_name in os.environ
        for variable_name in (
            "SLURM_NODEID",
            "SLURM_NNODES"
        )
    ])


def must_be_in_slurm_node():
    """Raises RuntimeError if we are not in a SLURM node."""
    if not is_slurm_node():
        raise RuntimeError(
            "The current execution is not running within "
            "a SLURM node. It is impossible to proceed with "
            "the current script."
        )


def get_slurm_node_id() -> int:
    """Return node ID of current SLURM node.

    Raises
    ---------------------
    RuntimeError
        If we are not currently in SLURM cluster.
    """
    must_be_in_slurm_node()
    return int(os.environ["SLURM_NODEID"])


def get_number_of_available_slurm_nodes() -> int:
    """Return number of available SLURM nodes.

    Raises
    ---------------------
    RuntimeError
        If we are not currently in SLURM cluster.
    """
    must_be_in_slurm_node()
    return int(os.environ["SLURM_NNODES"])
