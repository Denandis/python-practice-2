"""Assessment example: operand order matters for subtraction."""

from calculator import subtract


def test_subtract():
    """Subtraction returns the first number minus the second."""
    result = subtract(5, 3)
    assert result == 2
    