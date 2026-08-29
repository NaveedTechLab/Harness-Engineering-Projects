"""cart.py — the shopping cart. This is where the real bug lives."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pricing import get_unit_price


def calculate_order_total(items: dict) -> float:
    """Calculate the total price for an order.

    items: a dict mapping item_name -> quantity.
    Returns the total price as a float (unit_price * quantity, summed
    across all items).

    calculate_order_total({"widget": 2, "gadget": 1}) -> 34.48
    (2 * 9.99 + 1 * 14.50)
    """
    total = 0.0
    for name, qty in items.items():
        price = get_unit_price(name)
        total += price * qty
    return total
