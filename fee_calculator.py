
"""Library late-fee calculator with input validation."""

FEE_RATES = {
    "book": 0.25,
    "dvd": 1.00,
    "magazine": 0.25,
}


def calculate_fee(
    item_type: str,
    days_overdue: int,
    student: bool = False,
) -> float:
    """Calculate a library item's late fee in Canadian dollars."""
    if not isinstance(days_overdue, int) or isinstance(days_overdue, bool):
        raise ValueError("Overdue days must be an integer")

    if days_overdue < 0:
        raise ValueError("Overdue days cannot be negative")

    if not isinstance(item_type, str):
        raise ValueError("Unsupported item type")

    item = item_type.strip().lower()

    if item not in FEE_RATES:
        raise ValueError("Unsupported item type")

    fee = days_overdue * FEE_RATES[item]

    if student:
        fee *= 0.5

    return round(fee, 2)


def format_fee(fee: float) -> str:
    """Format a Canadian-dollar fee for display."""
    return f"Late fee: ${fee:.2f} CAD"
