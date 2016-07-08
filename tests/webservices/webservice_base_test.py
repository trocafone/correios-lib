from unittest import TestCase
from correios_lib.webservices import WebserviceBase, WebserviceError


class StubWebserviceBase(WebserviceBase):

    def get_env(self, env):
        environments = {
            'DEV': 'http://webservicescolhomologacao.correios.com.br/'
            'ScolWeb/WebServiceScol?wsdl'
        }
        return environments[env]


class TestWebserviceBase(TestCase):

    def setUp(self):
        self.webservice = StubWebserviceBase(
            env='DEV',
            id_correios='empresacws',
            password='123456'
        )

    def test_not_implemented_get_env(self):
        self.assertRaises(
            NotImplementedError,
            WebserviceBase,
            'DEV',
            'empresacws',
            '123456'
        )

    def test_nonexisting_method(self):
        self.assertRaises(
            WebserviceError,
            self.webservice.call,
            'test',
            {'test'}
        )
