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

from suds.client import Client


class WebserviceError(Exception):
    pass


class WebserviceBase():

    def __init__(self, env):
        ''' Depending on the env get a different wsdl definition

        :env: str - Environment used to get the wsdl
        '''
        self.client = Client(self.get_env(env))

    def get_env(self, env):
        """ Must be implemented in order to return the correct wsdl """
        raise NotImplementedError()

    def call(self, method, request):
        ''' Call the webservice method with the validated request content

        :method: str - Name of the method available at the webservice
        :request: RequestObject - Object containing all the info needed
        '''
        service_method = getattr(self.client.service, method, None)

        if service_method is None:
            available_services = [
                x[0] for x in self.client.wsdl.messages.keys()
                if x[0].find('Response') is -1
            ]
            raise WebserviceError('The method you are trying to call does not '
                                  'exists. Only the following methods are '
                                  'available {0}'.format(
                                      str(available_services)
                                  ))

        return service_method(request)
