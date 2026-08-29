"""
legacy/old_cart.py — DEPRECATED, unused.

This file has a function with a suspiciously similar name to the real
bug's function (calculate_total vs calculate_order_total). It exists to
test whether a search finds the RIGHT function or gets confused by a
similarly-named decoy. This file is not imported anywhere and is not
part of the live codebase.
"""


def calculate_total(cart_items):
    # Old implementation from a previous version of the app. Do not use.
    return sum(cart_items.values())
