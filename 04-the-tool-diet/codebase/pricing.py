"""pricing.py — price lookups for the shopping cart."""


def get_unit_price(item_name: str) -> float:
    prices = {"widget": 9.99, "gadget": 14.50, "gizmo": 3.25}
    return prices.get(item_name, 0.0)
