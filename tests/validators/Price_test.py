from correios_lib.validators import Price
from voluptuous import Invalid
from unittest import TestCase


class TestPrice(TestCase):

    def setUp(self):
        self.invalid_cases = ['1111.1', '000000000000001']
        self.valid_cases = [10, 10.123123]

    def test_invalid_prices(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, Price, i)

    def test_valid_prices(self):
        for i in self.valid_cases:
            self.assertTrue(Price(i))
