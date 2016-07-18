# -*- coding: utf-8 -*-
from correios_lib.entities import Objeto
from unittest import TestCase
from voluptuous import MultipleInvalid


class ObjetoTest(TestCase):

    def setUp(self):
        self.valid_cases = [
            (
                {'item': 1, 'id': '123', 'desc': 'a nice prod'},
                {'item': 1, 'id': '123', 'desc': 'a nice prod'}
            ),
            ({'item': 1}, {'item': 1})
        ]

    def test_invalid_objetos(self):
        self.assertRaises(MultipleInvalid, Objeto, id='1')
        self.assertRaises(MultipleInvalid, Objeto, item=None)

    def test_valid_objetos(self):
        for i in self.valid_cases:
            self.assertEquals(i[1], Objeto(**i[0]))
