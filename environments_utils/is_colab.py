"""Submodule providing utilities relative to detecting whether the script is whithin a Jupyter Notebook on Google COLAB."""


def is_colab() -> bool:
    """Return a boolean representing if script is running within a jupyter notebook on Google COLAB."""
    try:
        import google.colab  # pylint: disable=import-outside-toplevel unused-import import-error no-name-in-module

        return True
    except:  # pylint: disable=bare-except
        return False
