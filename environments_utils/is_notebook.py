"""Submodule providing utilities relative to detecting whether the script is whithin a Jupyter Notebook."""


def is_notebook() -> bool:
    """Return a boolean representing if script is running within a jupyter notebook.
    
    Implementative details
    ----------------------
    This function DOES NOT return True when running the script on Google Colab.
    Please use `is_colab` instead for those cases.
    """
    try:
        return get_ipython().__class__.__name__ == 'ZMQInteractiveShell'
    except NameError:
        pass
    return False
