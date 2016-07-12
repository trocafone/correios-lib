# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Trocafone
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################

from correios_lib.entities import EntityBase
from voluptuous import Schema
from unittest import TestCase
from unittest.mock import Mock


class EntityBaseTest(TestCase):

    def test_non_implemented_schema(self):
        entity = EntityBase({'test1': 123})
        self.assertRaises(
            NotImplementedError,
            entity.validate
        )

    def test_success_validating_entity(self):
        entity = EntityBase({'test1': 123, 'test2': 'abc'})
        entity.get_schema = Mock(
            return_value=Schema({'test1': int, 'test2': str})
        )

        self.assertTrue(entity.validate())

    def test_insuccess_validating_entity(self):
        entity = EntityBase({'test1': 123, 'test2': 'abc'})
        entity.get_schema = Mock(
            return_value=Schema({'test1': str, 'test2': str})
        )

        self.assertFalse(entity.validate())
        self.assertEquals(
            str(entity.error),
            "expected str for dictionary value @ data['test1']"
        )
