"""Tests for the package version."""

from validate_version_code import validate_version_code
from environments_utils.__version__ import __version__


def test_version():
    """Test whether the package version is valid."""
    assert validate_version_code(__version__)
