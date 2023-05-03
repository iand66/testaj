import pytest
from pay.order import LineItem, Order
from pay.payment import pay_order
from pytest import MonkeyPatch

from pay.processor import PaymentProcessor

def test_valid_pay_order(monkeypatch:MonkeyPatch) -> None:
    def charge_mock(self, card: str, month: int, year: int, amount: int) -> None:
       pass
    inputs = ['1249190007575069','12','2022']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, '_check_api_key', lambda _: True)
    monkeypatch.setattr(PaymentProcessor, 'charge', charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)

def test_invalid_pay_order(monkeypatch:MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        def charge_mock(self, card: str, month: int, year: int, amount: int) -> None:
            pass
        inputs = ['1249190007575069','12','2022']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, '_check_api_key', lambda _: True)
        monkeypatch.setattr(PaymentProcessor, 'charge', charge_mock)
        order = Order()
        pay_order(order)