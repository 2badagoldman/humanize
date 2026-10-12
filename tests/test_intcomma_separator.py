"""Tests for the `separator` argument of `humanize.intcomma`."""

from __future__ import annotations

import math

import pytest

import humanize


@pytest.mark.parametrize(
    "test_args, kwargs, expected",
    [
        ([1234567], {"separator": "."}, "1.234.567"),
        ([1234567], {"separator": " "}, "1 234 567"),
        ([1234567], {"separator": ""}, "1234567"),
        ([1234567], {"separator": "--"}, "1--234--567"),
        ([1234.5], {"separator": "--"}, "1--234.5"),
        ([1234567], {"separator": "_"}, "1_234_567"),
        ([1234567], {"separator": None}, "1,234,567"),
        ([100], {"separator": "."}, "100"),
        ([1000], {"separator": "."}, "1.000"),
        ([999], {"separator": "."}, "999"),
        ([-1234567], {"separator": "."}, "-1.234.567"),
        ([-1234567], {"separator": " "}, "-1 234 567"),
        ([1234.5], {"separator": " "}, "1 234.5"),
        ([1234567.25], {"separator": "."}, "1.234.567.25"),
        ([1234.5454545, 2], {"separator": " "}, "1 234.55"),
        ([1234.5454545, 2], {"separator": "'"}, "1'234.55"),
        ([1234.5454545], {"separator": " ", "ndigits": 2}, "1 234.55"),
        ([0], {"separator": "."}, "0"),
        ([-999], {"separator": "."}, "-999"),
        ([-1000], {"separator": "."}, "-1.000"),
        ([1234.5454545], {"separator": " ", "ndigits": 0}, "1 235"),
        (["1234567"], {"separator": "."}, "1.234.567"),
        (["-1234.5"], {"separator": " "}, "-1 234.5"),
        (["14308.40", 1], {"separator": "."}, "14.308.4"),
        ([None], {"separator": "."}, "None"),
        ([math.nan], {"separator": "."}, "NaN"),
        (["nan"], {"separator": "."}, "NaN"),
        ([float("inf")], {"separator": " "}, "+Inf"),
    ],
)
def test_intcomma_separator(
    test_args: list[int] | list[float] | list[str],
    kwargs: dict[str, str | int | None],
    expected: str,
) -> None:
    assert humanize.intcomma(*test_args, **kwargs) == expected


def test_intcomma_separator_is_keyword_only() -> None:
    with pytest.raises(TypeError):
        humanize.intcomma(1234567, None, ".")  # type: ignore[misc]


@pytest.mark.parametrize("sign", [1, -1])
def test_intcomma_large_integer_separator(sign: int) -> None:
    value = sign * (10**400 + 123)
    expected = ("-" if sign < 0 else "") + "10" + ".000" * 132 + ".123"
    assert humanize.intcomma(value, separator=".") == expected
