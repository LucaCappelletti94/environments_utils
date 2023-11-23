"""Module to try and run the rosetta detection function."""
from environments_utils import is_macos_rosetta
from environments_utils import is_windows, is_linux, is_arm


def test_is_macos_rosetta() -> None:
    """Test is_macos_rosetta."""
    if is_windows():
        assert not is_macos_rosetta()
    if is_linux():
        assert not is_macos_rosetta()
    if is_arm():
        assert not is_macos_rosetta()
