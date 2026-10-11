from __future__ import annotations

import humanize
import pytest


@pytest.mark.parametrize(
    "value, fmt, expected",
    [
        (10**24 - 1, "%.1f", "1.0 septillion"),
        (10**24 - 1, "%.0f", "1 septillion"),
        (999_999_999, "%.1f", "1.0 billion"),
        (999_950_000, "%.1f", "1.0 billion"),
        (-(10**24 - 1), "%.1f", "-1.0 septillion"),
        (10**6 - 1, "%.1f", "1.0 million"),
        (10**6 - 1, "%.0f", "1 million"),
        (10**9 - 1, "%.1f", "1.0 billion"),
        (10**9 - 1, "%.0f", "1 billion"),
        (10**12 - 1, "%.1f", "1.0 trillion"),
        (10**12 - 1, "%.0f", "1 trillion"),
        (10**15 - 1, "%.1f", "1.0 quadrillion"),
        (10**15 - 1, "%.0f", "1 quadrillion"),
        (10**18 - 1, "%.1f", "1.0 quintillion"),
        (10**18 - 1, "%.0f", "1 quintillion"),
        (10**21 - 1, "%.1f", "1.0 sextillion"),
        (10**21 - 1, "%.0f", "1 sextillion"),
        (10**24 - 1, "%.1f", "1.0 septillion"),
        (10**24 - 1, "%.0f", "1 septillion"),
        (10**27 - 1, "%.1f", "1.0 octillion"),
        (10**27 - 1, "%.0f", "1 octillion"),
        (10**30 - 1, "%.1f", "1.0 nonillion"),
        (10**30 - 1, "%.0f", "1 nonillion"),
        (10**33 - 1, "%.1f", "1.0 decillion"),
        (10**33 - 1, "%.0f", "1 decillion"),
    ],
)
def test_intword_carries_rounded_up_values(value: int, fmt: str, expected: str) -> None:
    assert humanize.intword(value, fmt) == expected


@pytest.mark.parametrize("fmt", ["%.0f", "%.1f", "%.2f"])
@pytest.mark.parametrize("exponent", range(6, 34))
def test_intword_number_below_1000(exponent: int, fmt: str) -> None:
    for value in (10**exponent - 1, 10**exponent - 10 ** (exponent - 4)):
        result = humanize.intword(value, fmt)
        assert float(result.split()[0]) < 1000, result


