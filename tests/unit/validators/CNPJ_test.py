from correios_lib.validators import CNPJ
from voluptuous import Invalid
from unittest import TestCase


class TestCNPJ(TestCase):

    def setUp(self):
        self.invalid_cases = ['00000000000000', '83.679.262/0001-5']
        self.valid_cases = ['83.679.262/0001-51', '83679262000151']

    def test_invalid_cnpjs(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, CNPJ, i)

    def test_valid_cnpjs(self):
        for i in self.valid_cases:
            self.assertTrue(CNPJ(i))
