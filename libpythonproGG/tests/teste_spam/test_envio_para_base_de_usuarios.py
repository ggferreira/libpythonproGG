from unittest.mock import Mock

import pytest

from libpythonproGG.spam.main import EnviadorDeSpam
from libpythonproGG.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabriel@ferreira_1@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel@ferreira.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@ferreira_1@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@ferreira_1@hotmail.com',
        'gabriel@ferreira.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
