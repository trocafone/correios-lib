from base import EntityBase
from entities import *
from voluptuous import *


class ReqSolicitarPostagemReversa(EntityBase):

    def get_schema(self):
        return Schema({
            Required('cod_administrativo'): Coerse(int),
            Required('cod_servico'): Coerse(int),
            Required('cartao'): Coerse(int),
            Required('destinatario'): Destinatario,
            Required('coletas_solicitadas'): [Coleta]
        })
