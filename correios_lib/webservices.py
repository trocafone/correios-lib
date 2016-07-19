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


from correios_lib.base import WebserviceBase


class LogisticaReversa(WebserviceBase):

    def get_env(self, env):
        envs = {
            'HOMOLOG': 'https://apphom.correios.com.br/logisticaReversaWS/'
                       'logisticaReversaService/logisticaReversaWS?wsdl',
            'PROD': 'https://cws.correios.com.br/logisticaReversaWS/'
                    'logisticaReversaService/logisticaReversaWS?wsdl',
        }

        return envs[env]

    def SolicitarPostagemReversa(self, request):
        return self.call("solicitarPostagemReversa", request)

    def SolicitarPostagemSimultanea(self, request):
        return self.call("solicitarPostagemSimultanea", request)

    def AcompanharPedido(self, request):
        return self.call('acompanharPedido', request)

    def AcompanharPedidoPorData(self, request):
        return self.call('acompanharPedidoPorData', request)

    def CancelarPedido(self, request):
        return self.call('cancelarPedido', request)

    def SolicitarRange(self, request):
        return self.call('solicitarRange', request)

    def CalcularDigitoVerificador(self, request):
        return self.call('calcularDigitoVerificador', request)
