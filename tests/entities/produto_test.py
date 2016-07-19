# -*- coding: utf-8 -*-
from correios_lib.entities import Produto
from unittest import TestCase
from voluptuous import MultipleInvalid


class ProdutoTest(TestCase):

    def setUp(self):
        self.valid_cases = [
            (
                {'codigo': '1', 'tipo': '123', 'qtd': '1'},
                {'codigo': 1, 'tipo': 123, 'qtd': 1},
            ),
            ({}, {})
        ]

    def test_invalid_products(self):
        self.assertRaises(MultipleInvalid, Produto, codigo='abc')

    def test_valid_products(self):
        for i in self.valid_cases:
            self.assertEquals(i[1], Produto(**i[0]))
