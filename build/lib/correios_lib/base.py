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
from voluptuous import Invalid, MultipleInvalid
import certifi
import logging.config


class WebserviceError(Exception):
    pass


class WebserviceBase():

    def __init__(self, env, id_correios, password,
                 cert=False, log_config=None):
        ''' Webservice initialization.

        Depending on the env get a different wsdl definition.
        New Correios SIGEP uses HTTPAuth to do requests.

        Args:
            env (str): Environment used to get the wsdl
            id_correios (str): IdCorreios given by correios website
            password (str): password vinculated to the IdCorreios
            log_config (dict): Dictionary configurations of logging
        '''

        ''' Untrusted ssl certificate for homolog envs see more at:

        https://www.ssllabs.com/ssltest/analyze.html?d=apphom.correios.com.br
        '''
        if cert is False:
            verify = False
        else:
            verify = certifi.where()

        if log_config is not None and isinstance(log_config, dict):
            """ Example config from zeep documentation:

            {
                'version': 1,
                'formatters': {
                    'verbose': {
                        'format': '%(name)s: %(message)s'
                    }
                },
                'handlers': {
                    'console': {
                        'level': 'DEBUG',
                        'class': 'logging.StreamHandler',
                        'formatter': 'verbose',
                    },
                },
                'loggers': {
                    'zeep.transports': {
                        'level': 'DEBUG',
                        'propagate': True,
                        'handlers': ['console'],
                    },
                }
            }
            """
            logging.config.dictConfig(log_config)

        t = Transport(
            verify=verify,
            http_auth=(id_correios, password)
        )
        self.client = Client(wsdl=self.get_env(env), transport=t)

    def get_env(self, env):
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

        Args:
            method (str): Name of the method available at the webservice
            request (RequestObject): Object containing all the info needed

        Returns:
            dict: Result of the service call
        '''
        service_method = getattr(self.client.service, method, None)

        req_type = 'Request' + method[0].upper() + method[1:]
        req_instance = request.__class__.__name__

        if req_type != req_instance:
            raise WebserviceError(
                'Request must be an instance of {0}, given {1}'.format(
                    req_type,
                    req_instance
                 )
            )

        import sys
        if sys.version_info <= (3, 0):
            reload(sys)
            sys.setdefaultencoding('utf-8')

        try:
            return service_method(**request)
        except ValueError as e:
            raise WebserviceError(e)


class EntityBase(dict):

    def __init__(self, **kargs):
        super(EntityBase, self).__init__(kargs)
        self.validate()

        try:
            raise getattr(self, 'error')
        except AttributeError:
            pass
        except Invalid as e:
            raise MultipleInvalid([e])

    def get_schema(self):
        """ Returns validation schema

        Returns:
            voluptous.Schema: Schema with validation rules
        """
        raise NotImplementedError("Every entitiy needs validation against a " +
                                  "Schema.")

    def validate(self):
        """ Validates content against schema

        In case of failure an error is kept inside the entity object,
        to be displayed by the client user if needed.

        Returns:
            bool: Validation result
        """
        schema = self.get_schema()
        try:
            super(EntityBase, self).__init__(schema(self))
            return True
        except Exception as e:
            self.error = e
            return False
