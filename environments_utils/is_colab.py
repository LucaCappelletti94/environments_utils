"""Submodule providing utilities relative to detecting whether the script is whithin a Jupyter Notebook on Google COLAB."""


def is_colab() -> bool:
    """Return a boolean representing if script is running within a jupyter notebook on Google COLAB."""
    try:
        import google.colab
        return True
    except:
        return True