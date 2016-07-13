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

from correios_lib.base import EntityBase
from voluptuous import Schema, Required, All, Length
from correios_lib.validators import CEP, Email


class Pessoa(EntityBase):
    def __init__(self, nome="", logradouro="", numero="", complemento="",
                 bairro="", referencia="", cidade="", uf="", cep="", ddd="",
                 telefone="", email=""):
        super(Pessoa, self).__init__(locals())

    def get_schema(self):
        self.schema = Schema({
            Required('nome'): All(str, Length(min=4)),
            Required('logradouro'): All(str, Length(min=4)),
            Required('numero'): All(str, Length(min=1)),
            'complemento': str,
            Required('bairro'): All(str, Length(min=2)),
            'referencia': str,
            Required('cidade'): All(str, Length(min=3)),
            Required('uf'): All(str, Length(min=2, max=2)),
            Required('cep'): All(CEP, Length(min=8, max=9)),
            'ddd': All(str, Length(min=2, max=2)),
            'telefone': All(str, Length(min=8, max=10)),
            'email': Email
        })
