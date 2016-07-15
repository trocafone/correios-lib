from unittest import TestCase
from correios_lib.webservices import LogisticaReversa
from correios_lib.entities import Remetente, Destinatario, Coleta, \
     Objeto, Produto
from correios_lib.requests import RequestSolicitarPostagemReversa


class LogisticaReversaTest(TestCase):
    def setUp(self):
        self.client = LogisticaReversa(
            env='HOMOLOG',
            id_correios='empresacws',
            password='123456',
            cert=False
        )

    def test_get_env(self):
        self.assertEquals(
            'https://apphom.correios.com.br/logisticaReversaWS/'
            'logisticaReversaService/logisticaReversaWS?wsdl',
            self.client.get_env('HOMOLOG')
        )
        self.assertEquals(
            'https://cws.correios.com.br/logisticaReversaWS/'
            'logisticaReversaService/logisticaReversaWS?wsdl',
            self.client.get_env('PROD')
        )

    def test_solicitar_postagem_reversa(self):
        request = RequestSolicitarPostagemReversa(
            codAdministrativo='08082650',
            codigo_servico='41076',
            cartao='0057018901',
            destinatario=Destinatario(
                nome='Fulano',
                logradouro='SBN',
                numero='10',
                complemento='Bloco A',
                bairro='Plano Piloto',
                cidade='Brasília',
                uf='DF',
                cep='70002900',
                ddd='61',
                telefone='34261111',
                email='fulano@mail.com'
            ),
            coletas_solicitadas=[
                Coleta(
                    tipo='A',
                    id_cliente='1133566',
                    valor_declarado=1500.00,
                    descricao="",
                    cklist=2,
                    documento=[],
                    remetente=Remetente(
                        nome='Ciclano',
                        logradouro='Rua 35',
                        numero='10',
                        complement='',
                        bairro='Águas Claras(Sul)',
                        referencia='',
                        cidade='Brasília',
                        uf='DF',
                        cep='71931180',
                        ddd='61',
                        telefone='34262222',
                        email='ciclano@mail.com',
                        identificacao='',
                        ddd_celular='61',
                        celular='92236666',
                        sms='S'
                    ),
                    produto=Produto(
                        codigo='116600063',
                        tipo='0',
                        qtd='1'
                    ),
                    ag=5,
                    cartao='',
                    servico_adicional='',
                    ar='',
                    obj_col=[
                        Objeto(
                            item=1,
                            desc='',
                            entrega='',
                            num='',
                            id='553366'
                        )
                    ]
                )
            ]
        )

        self.client.SolicitarPostagemReversa(request)
