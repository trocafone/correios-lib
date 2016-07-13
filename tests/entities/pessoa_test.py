from unittest import TestCase
from correios_lib.entities import Pessoa


class TestPessoa(TestCase):

    def setUp(self):
        self.entity = Pessoa()

    def test_invalid_pessoa(self):
        assert self.entity.validate() is False

    def test_valid_pessoa(self):
        pass
