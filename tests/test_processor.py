from pay.processor import PaymentProcessor
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor('')
        processor.charge('1249190007575069',12,2023,100)

def test_valid_card_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge('1249190007575069',12,2023,100)

def test_invalid_card_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge('1249190007575069',12,1023,100)

def test_valid_charge_amt() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge('1249190007575069',12,2023,100)

def test_invalid_charge_card() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge('1249190007575068',12,2023,100)

def test_valid_card_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum('1249190007575069')

def test_invalid_card_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum('1249190007575068')


