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

from voluptuous import Invalid
from brazilnum.util import clean_id
from brazilnum.cnpj import validate_cnpj
from brazilnum.cpf import validate_cpf
from brazilnum.cep import format_cep
import datetime
import re


def CNPJ(value):
    if not validate_cnpj(value):
        raise Invalid("Invalid CNPJ")
    return clean_id(value)


def CPF(value):
    if not validate_cpf(value):
        raise Invalid("Invalid CPF")
    return clean_id(value)


def CEP(value):
    try:
        format_cep(value)
    except ValueError as e:
        raise Invalid(e)

    return clean_id(value)


def Email(value):
    if not re.match("[^@]+@[^@]+\.[^@]+", value):
        raise Invalid("This email is invalid.")
    return value


def Date(value):
    fmt = '%d/%m/%Y'
    try:
        if isinstance(value, int):
            value = datetime.date.today() + datetime.timedelta(value)

        return value.strftime(fmt)
    except Exception:
        raise Invalid("Should be an instance of datetime.datetime")


def Price(value):
    if not (type(value) == int or type(value) == float):
        raise Invalid("This price is not and integer or a float.")
    value = float(value)
    return "%.2f" % value
