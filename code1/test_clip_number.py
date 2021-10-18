from clip_number import clip_number
import pytest

@pytest.mark.parametrize("number, min_value, max_value, output",
    [(0.58, 0, 1, 0.58), (3.25, 1, 0, 1), (-0.5, 0, 1, 0), (0.01, 0, 1, 0.01)])
def test_clip_number(number,min_value, max_value, output):
    assert (clip_number(number, min_value, max_value) == output)
