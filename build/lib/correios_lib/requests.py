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
from correios_lib.entities import *
from voluptuous import *


class RequestSolicitarPostagemReversa(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('codigo_servico'): Coerce(int),
            Required('cartao'): Coerce(int),
            Required('destinatario'): Destinatario,
            Required('coletas_solicitadas'): [Coleta]
        }, extra=REMOVE_EXTRA)


class RequestSolicitarPostagemSimultanea(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('codigo_servico'): Coerce(int),
            Required('cartao'): Coerce(int),
            Required('destinatario'): Destinatario,
            Required('coletas_solicitadas'): [ColetaSimultanea]
        }, extra=REMOVE_EXTRA)


class RequestCancelarPedido(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('numeroPedido'): Coerce(int),
            Required('tipo'): Any('C', 'A')
        }, extra=REMOVE_EXTRA)


class RequestAcompanharPedido(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('tipoBusca'): Any('H', 'U'),
            Required('numeroPedido'): Coerce(int),
            Required('tipoSolicitacao'): Any('C', 'A')
        }, extra=REMOVE_EXTRA)


class RequestAcompanharPedidoPorData(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('tipoSolicitacao'): Any('C', 'A'),
            Required('data'): Date
        }, extra=REMOVE_EXTRA)


class RequestSolicitarRange(EntityBase):

    def get_schema(self):
        return Schema({
            Required('codAdministrativo'): Coerce(int),
            Required('tipo'): Any('AP', 'LR'),
            Optional('servico'): Any('LR', 'LS', 'LV'),
            Required('quantidade'): All(
                Coerce(int), Range(min=1, max=100000)
            )
        }, extra=REMOVE_EXTRA)


class RequestCalcularDigitoVerificador(EntityBase):

    def get_schema(self):
        return Schema({
            Required('numero'): Coerce(int),
        }, extra=REMOVE_EXTRA)
