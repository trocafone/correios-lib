# -*- coding: utf-8 -*-
from correios_lib.entities import Coleta, Remetente
from unittest import TestCase
from voluptuous import MultipleInvalid


class ColetaTest(TestCase):

    def setUp(self):
        self.valid_cases = [
            (
                {
                    'tipo': 'C',
                    'remetente': Remetente(
                        nome='Name',
                        logradouro='My Street',
                        numero=123,
                        bairro='My neighborhood',
                        cidade='My City',
                        uf='SP',
                        cep='01508020',
                        ddd=11,
                        telefone='12312311',
                        email='emailforwarning@email.com'
                    )
                },
                {
                    'tipo': 'C',
                    'remetente': Remetente(
                        nome='Name',
                        logradouro='My Street',
                        numero=123,
                        bairro='My neighborhood',
                        cidade='My City',
                        uf='SP',
                        cep='01508020',
                        ddd=11,
                        telefone='12312311',
                        email='emailforwarning@email.com'
                    )
                }
            )
        ]

    def test_invalid_coletas(self):
        self.assertRaises(MultipleInvalid, Coleta, codigo='abc')

    def test_valid_coletas(self):
        for i in self.valid_cases:
            self.assertEquals(i[1], Coleta(**i[0]))
