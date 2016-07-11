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

from zeep import Client
from zeep.transports import Transport
import certifi


class WebserviceError(Exception):
    pass


class WebserviceBase():

    def __init__(self, env: str, id_correios: str, password: str, cert=False):
        ''' Webservice initialization.

        Depending on the env get a different wsdl definition.
        New Correios SIGEP uses HTTPAuth to do requests.

        Args:
            env (str): Environment used to get the wsdl
            id_correios (str): IdCorreios given by correios website
            password (str): password vinculated to the IdCorreios
        '''

        ''' Untrusted ssl certificate for homolog envs see more at:

        https://www.ssllabs.com/ssltest/analyze.html?d=apphom.correios.com.br
        '''
        if cert is False:
            verify = False
        else:
            verify = certifi.where()

        t = Transport(
            verify=verify,
            http_auth=(id_correios, password)
        )
        self.client = Client(wsdl=self.get_env(env), transport=t)

    def get_env(self, env: str) -> str:
        """ Get WSDL Url.

        Must be implemented in order to return the correct WSDL.

        Args:
            env (str): Environment used to get the wsdl

        Returns:
            str: WSDL Url of the corresponding environment
        """
        raise NotImplementedError()

    def call(self, method, request):
        ''' Call the webservice method with the validated request content

        :method: str - Name of the method available at the webservice
        :request: RequestObject - Object containing all the info needed
        '''
        service_method = getattr(self.client.service, method, None)

        try:
            return service_method(request)
        except ValueError:
            raise WebserviceError('The method you are trying to call does not '
                                  'exists.')
