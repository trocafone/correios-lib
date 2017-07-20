from correios_lib.validators import Date
from voluptuous import Invalid
from unittest import TestCase
import datetime


class TestDate(TestCase):

    def setUp(self):
        self.invalid_cases = ['2015/1/2', None]
        value = datetime.date.today() + datetime.timedelta(5)
        self.valid_cases = [
            (datetime.date(2016, 1, 2), '02/01/2016'),
            (5, value.strftime('%d/%m/%Y'))
        ]

    def test_invalid_dates(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, Date, i)

    def test_valid_dates(self):
        for i in self.valid_cases:
            self.assertEquals(i[1], Date(i[0]))
