import pytest

from libpythonproGG.spam.enviador_de_email import Enviador
from libpythonproGG.spam.main import EnviadorDeSpam
from libpythonproGG.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_emails_enviador = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviador += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gabriel', email='gabriel@ferreira.com'),
            Usuario(nome='Luciano', email='gabriel@ferreira.com'),
        ],
        [
            Usuario(nome='Gabriel', email='gabriel@ferreira.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabriel@ferreira_1@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviador


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel@ferreira.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@ferreira_1@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'luciano@ferreira_1@hotmail.com',
        'gabriel@ferreira.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
