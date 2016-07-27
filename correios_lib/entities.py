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
from correios_lib.validators import CEP, Email, Date, Price
from voluptuous import *


class Destinatario(EntityBase):
    ''' Reference to wsdl: '''

    def get_schema(self):
        return Schema({
            Required('nome'): All(Coerce(str), Length(max=60)),
            Required('logradouro'): All(Coerce(str), Length(max=72)),
            Required('numero'): All(Coerce(str), Length(max=8)),
            Optional('complemento'): All(Coerce(str), Length(max=30)),
            Required('bairro'): All(Coerce(str), Length(max=50)),
            Optional('referencia'): All(Coerce(str), Length(max=60)),
            Required('cidade'): All(Coerce(str), Length(max=36)),
            Required('uf'): All(Coerce(str), Length(min=2, max=2)),
            Required('cep'): All(CEP, Length(min=8, max=9)),
            Optional('ddd'): All(Coerce(str), Length(min=2, max=2)),
            Optional('telefone'): All(Coerce(str), Length(min=8, max=12)),
            Optional('email'): All(Email, Length(max=72))
        }, extra=REMOVE_EXTRA)


class Coleta(EntityBase):

    def get_schema(self):
        return Schema({
            Required('tipo'): Any('CA', 'C', 'A'),
            Optional('numero'): Coerce(int),
            Optional('id_cliente'): All(Length(max=30)),
            Optional('ag'): Date,
            Optional('cartao'): Coerce(str),
            Optional('valor_declarado'): Price,
            Optional('servico_adicional'): All(Coerce(str), Length(max=20)),
            Optional('descricao'): All(Coerce(str), Length(max=255)),
            Optional('ar'): Any(1, 0),
            Optional('cklist'): Any(2, 4, 5, 7),
            Optional('documento'): [str],
            Required('remetente'): Remetente,
            Optional('obj_col'): [Objeto],
            Optional('produto'): Produto
        }, extra=REMOVE_EXTRA)


class ColetaSimultanea(EntityBase):

    def get_schema(self):
        return Schema({
            Required('tipo'): Any('C', 'A'),
            Optional('id_cliente'): All(Length(max=30)),
            Optional('valor_declarado'): Price,
            Optional('descricao'): All(Coerce(str), Length(max=255)),
            Optional('cklist'): Any(2, 4, 5, 7),
            Optional('documento'): [str],
            Required('remetente'): Remetente,
            Optional('produto'): Produto,
            Optional('obs'): All(Coerce(str))
        }, extra=REMOVE_EXTRA)


class Objeto(EntityBase):

    def get_schema(self):
        return Schema({
            Required('item'): 1,
            Optional('id'): All(Coerce(str), Length(max=30)),
            Optional('desc'): All(Coerce(str), Length(max=255)),
            Optional('entrega'): All(Coerce(str), Length(max=13)),
            Optional('num'): All(Coerce(str), Length(max=13)),
        }, extra=REMOVE_EXTRA)


class Produto(EntityBase):

    def get_schema(self):
        return Schema({
            Optional('codigo'): Coerce(int),
            Optional('tipo'): Coerce(int),
            Optional('qtd'): Coerce(int)
        }, extra=REMOVE_EXTRA)


class Remetente(EntityBase):

    def get_schema(self):
        return Schema({
            Required('nome'): All(Coerce(str), Length(max=60)),
            Required('logradouro'): All(Coerce(str), Length(max=72)),
            Required('numero'): All(Coerce(str), Length(max=8)),
            Optional('complemento'): All(Coerce(str), Length(max=30)),
            Required('bairro'): All(Coerce(str), Length(max=50)),
            Optional('referencia'): All(Coerce(str), Length(max=60)),
            Required('cidade'): All(Coerce(str), Length(max=36)),
            Required('uf'): All(Coerce(str), Length(min=2, max=2)),
            Required('cep'): All(CEP, Length(min=8, max=9)),
            Required('ddd'): All(Coerce(str), Length(min=2, max=2)),
            Required('telefone'): All(Coerce(str), Length(min=8, max=12)),
            Required('email'): All(Email, Length(max=72)),
            Optional('celular'): All(Coerce(str), Length(max=9)),
            Optional('ddd_celular'): All(Coerce(str), Length(max=3)),
            Optional('sms'): Any('S', 'N'),
            Optional('identificacao'): All(Coerce(str), Length(max=14))
        }, extra=REMOVE_EXTRA)
