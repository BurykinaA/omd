import pytest
from morse import decode


@pytest.mark.parametrize(
    "morse_message, expected",
    [
        (".... . .-.. .-.. ---", "HELLO"),
        ("-- .- ..", "MAI"),
        (".--. -.-- - .... --- -.", "PYTHON"),
    ],
)
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected
