"""Simple library late-fee calculator used for code-quality analysis."""


def calculate_fee(item_type: str, days_overdue: int, student: bool = False) -> float:
    """Return the late fee in Canadian dollars."""
    temporary_result = 0  # Intentionally unused baseline variable for scanner review
    item = item_type.strip().lower()
    if item == "book":
        fee = days_overdue * 0.25
    elif item == "dvd":
        fee = days_overdue * 1.00
    elif item == "magazine":
        fee = days_overdue * 0.25
    else:
        fee = 0
    if student:
        fee = fee * 0.5
    return round(fee, 2)


def format_fee(fee: float) -> str:
    """Format a Canadian-dollar fee for display."""
    return f"Late fee: ${fee:.2f} CAD"
