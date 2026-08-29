"""fix_correct.py — a genuinely correct fix for stats.py's median bug."""


def median(numbers: list) -> float:
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]
