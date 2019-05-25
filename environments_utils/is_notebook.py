def is_notebook()->bool:
    """Return a boolean representing if script is running within a jupyter notebook."""
    try:
        return get_ipython().__class__.__name__ == 'ZMQInteractiveShell'
    except NameError:
        pass
    return False