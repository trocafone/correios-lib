from correios_lib.validators import Email
from voluptuous import Invalid
from unittest import TestCase


class TestEmail(TestCase):

    def setUp(self):
        self.invalid_cases = ['test.email.com', '000000000000000']
        self.valid_cases = ['test.email@correios.com', 'x@xxx.com']

    def test_invalid_emails(self):
        for i in self.invalid_cases:
            self.assertRaises(Invalid, Email, i)

    def test_valid_emails(self):
        for i in self.valid_cases:
            self.assertTrue(Email(i))
