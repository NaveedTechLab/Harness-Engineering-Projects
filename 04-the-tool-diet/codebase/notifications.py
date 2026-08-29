"""notifications.py — sends order confirmation emails.

Completely unrelated to this project's bug. Its only purpose is to be a
plausible-looking distraction: a broad-toolset agent might waste calls
opening this file "just in case" it's relevant.
"""


def send_confirmation_email(order_id: str) -> None:
    print(f"Pretending to email a confirmation for order {order_id}.")
