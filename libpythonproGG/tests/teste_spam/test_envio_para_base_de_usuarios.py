from libpythonproGG.spam.enviador_de_email import Enviador
from libpythonproGG.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gabriel@ferreira_1@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )