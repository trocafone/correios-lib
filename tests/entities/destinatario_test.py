# -*- coding: utf-8 -*-
from unittest import TestCase
from voluptuous import MultipleInvalid
from correios_lib.entities import Destinatario


class TestDestinatario(TestCase):

    def test_invalid_destinatario(self):
        self.assertRaises(MultipleInvalid, Destinatario)

    def test_valid_destinatario(self):
        self.entity = Destinatario(
            nome="Myname",
            logradouro="Rua Pretty cool",
            numero="123",
            bairro="Neighborhood",
            cidade="MyCity",
            uf="SP",
            cep="01508020",
            email="myemail@test.com"
        )
