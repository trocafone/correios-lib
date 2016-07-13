from correios_lib.validators import CEP
from voluptuous import Invalid
from unittest import TestCase


class TestCEP(TestCase):

    def setUp(self):
        self.invalid_cases = ['wqasd', 'aasasdasda', '00000000000', '111']
        self.valid_cases = ['01508020']

    def test_invalid_ceps(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, CEP, i)

    def test_valid_ceps(self):
        for i in self.valid_cases:
            self.assertTrue(CEP(i))
