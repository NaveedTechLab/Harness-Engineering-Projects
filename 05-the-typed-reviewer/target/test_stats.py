import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from stats import median


def test_median_unsorted_odd():
    assert median([5, 1, 3]) == 3


def test_median_unsorted_even():
    assert median([4, 1, 3, 2]) == 2.5


def test_median_already_sorted():
    assert median([1, 2, 3]) == 2
