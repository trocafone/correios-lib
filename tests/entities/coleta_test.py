from correios_lib.entities import Coleta, Remetente
from unittest import TestCase
from voluptuous import MultipleInvalid


class ColetaTest(TestCase):

    def setUp(self):
        self.valid_cases = [
            (
                {'tipo': 'C', 'remetente': },
                {'codigo': 1, 'tipo': 123, 'qtd': 1},
            ),
            ({}, {})
        ]

    def test_invalid_coletas(self):
        self.assertRaises(MultipleInvalid, Produto, codigo='abc')

    def test_valid_coletas(self):
        for i in self.valid_cases:
            self.assertEquals(i[1], Produto(**i[0]))
