"""Automated tests for expected library fee calculations."""
from fee_calculator import calculate_fee, format_fee


def test_book_happy_path():
    assert calculate_fee("book", 4) == 1.00


def test_dvd_happy_path():
    assert calculate_fee("DVD", 3) == 3.00


def test_student_discount():
    assert calculate_fee("book", 4, student=True) == 0.50


def test_magazine_fee():
    assert calculate_fee("magazine", 2) == 0.50


def test_output_format():
    assert format_fee(1) == "Late fee: $1.00 CAD"


import pytest


def test_negative_overdue_days():
    with pytest.raises(ValueError, match="negative"):
        calculate_fee("book", -2)


def test_invalid_item_type():
    with pytest.raises(ValueError, match="Unsupported"):
        calculate_fee("newspaper", 3)

