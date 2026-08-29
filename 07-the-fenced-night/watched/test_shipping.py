import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from shipping import calculate_shipping


def test_shipping_normal():
    assert calculate_shipping(2, 100) == pytest.approx(20.0)


def test_shipping_negative_weight_raises():
    with pytest.raises(ValueError):
        calculate_shipping(-1, 100)


def test_shipping_negative_distance_raises():
    with pytest.raises(ValueError):
        calculate_shipping(1, -100)
