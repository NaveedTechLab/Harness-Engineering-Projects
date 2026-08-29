"""inventory.py — stock checks. Not related to the bug in this project."""


def is_in_stock(item_name: str) -> bool:
    stock = {"widget": 10, "gadget": 0, "gizmo": 5}
    return stock.get(item_name, 0) > 0
