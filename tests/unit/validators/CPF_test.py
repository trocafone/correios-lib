from correios_lib.validators import CPF
from voluptuous import Invalid
from unittest import TestCase


class TestCPF(TestCase):

    def setUp(self):
        self.invalid_cases = ['648.152.363-05111', '000000000000000']
        self.valid_cases = ['648.152.363-05', '64815236305']

    def test_invalid_cnpjs(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, CPF, i)

    def test_valid_cnpjs(self):
        for i in self.valid_cases:
            self.assertTrue(CPF(i))
