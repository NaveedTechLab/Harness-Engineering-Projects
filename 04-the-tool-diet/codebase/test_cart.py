import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cart import calculate_order_total


def test_calculate_order_total():
    assert calculate_order_total({"widget": 2, "gadget": 1}) == pytest.approx(34.48)


def test_single_item():
    assert calculate_order_total({"gizmo": 4}) == pytest.approx(13.0)
