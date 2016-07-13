from unittest import TestCase
from voluptuous import MultipleInvalid
from correios_lib.entities import Pessoa


class TestPessoa(TestCase):

    def test_invalid_pessoa(self):
        self.assertRaises(MultipleInvalid, Pessoa)

    def test_valid_pessoa(self):
        self.entity = Pessoa(
            nome="Myname",
            logradouro="Rua Pretty cool",
            numero="123",
            bairro="Neighborhood",
            cidade="MyCity",
            uf="SP",
            cep="01508020",
            email="myemail@test.com"
        )
