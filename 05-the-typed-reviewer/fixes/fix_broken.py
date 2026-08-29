"""fix_broken.py — LOOKS like a fix, but has a classic subtle bug:
calls sorted(numbers) without capturing the return value. sorted()
doesn't sort in place — it returns a new sorted list. Since the result
is thrown away, `numbers` is never actually sorted, so this still fails
the exact same tests as the original bug."""


def median(numbers: list) -> float:
    sorted(numbers)  # BUG: return value discarded, numbers is unchanged
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]
