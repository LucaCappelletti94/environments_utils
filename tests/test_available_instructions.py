"""Test whether the methods in the available_instructions submodule are working."""
import pytest

from environments_utils import get_macos_available_instructions, is_macos


def test_macos_available_instructions():
    """Test the `get_macos_available_instructions` method."""
    if is_macos():
        available_instructions = get_macos_available_instructions()
        assert isinstance(available_instructions, list)
        assert len(available_instructions) > 0
        assert isinstance(available_instructions[0], str)
    else:
        with pytest.raises(NotImplementedError):
            get_macos_available_instructions()
