"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class TestItem:
    def test_init_item(self, item):
        assert item.price == 10000.0
        assert item.name == "Смартфон"
        assert item.quantity == 20
        assert Item.all == [item]

    def test_calculate_total_price(self, item):
        assert isinstance(item.calculate_total_price(), float)
        assert item.calculate_total_price() == 200000.0

    def test_apply_discount(self, item):
        item.pay_rate = 0.8
        item.apply_discount()
        assert item.price == 8000.0
