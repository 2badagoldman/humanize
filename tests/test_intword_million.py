from __future__ import annotations

import humanize


def test_intword_carries_into_million() -> None:
    assert humanize.intword(999_999) == "1.0 million"
    assert humanize.intword(999_999, "%.0f") == "1 million"
    assert humanize.intword(999_000) == "999.0 thousand"
