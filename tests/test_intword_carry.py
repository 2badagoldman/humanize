"""Regression tests: intword must carry to the next unit when rounding."""

from __future__ import annotations

import humanize
import pytest
from humanize import number


@pytest.mark.parametrize("exp", range(6, 33, 3))
def test_intword_carries_to_next_unit(exp: int) -> None:
    next_unit = number.human_powers[exp // 3 - 1][0]
    value = 10**exp - 1
    assert humanize.intword(value) == f"1.0 {next_unit}"
    assert humanize.intword(value, "%.0f") == f"1 {next_unit}"
    assert humanize.intword(-value) == f"-1.0 {next_unit}"
    assert humanize.intword(10**exp) == f"1.0 {next_unit}"


def test_intword_gap_above_decillion() -> None:
    assert humanize.intword(10**33 - 1) == "1.0 decillion"
    assert humanize.intword(10**36) == "1000.0 decillion"
    assert humanize.intword(2 * 10**100) == "2.0 googol"
