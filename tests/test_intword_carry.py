from __future__ import annotations

import pytest

import humanize
from humanize import number


@pytest.mark.parametrize("exp", range(6, 34, 3))
def test_intword_carries_to_next_unit(exp: int) -> None:
    # Values just below a power of 1000 must carry to the next unit.
    value = 10**exp - 1
    unit = number.human_powers[number.powers.index(10**exp) + 0][0]
    assert humanize.intword(value) == f"1.0 {unit}"
    assert humanize.intword(value, "%.0f") == f"1 {unit}"
    assert humanize.intword(-value, "%.0f") == f"-1 {unit}"
    # Not rounded up: stays in the lower unit and never reaches 1000.
    assert not humanize.intword(10**exp - 10 ** (exp - 3) * 2).startswith("1000")


def test_intword_septillion_regression() -> None:
    assert humanize.intword(10**24 - 1) == "1.0 septillion"
    assert humanize.intword(10**24 - 1, "%.0f") == "1 septillion"
    assert humanize.intword(10**36) == "1000.0 decillion"
    assert humanize.intword(2 * 10**100) == "2.0 googol"
