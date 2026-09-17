"""Assessment example: verify a returned value with an assertion."""

from calculator import add


def test_add():
    """Adding two positive integers returns their sum."""
    result = add(2, 3)
    assert result == 5