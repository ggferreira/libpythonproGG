from libpythonproGG.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel@ferreira.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Gabriel', email='gabriel@ferreira.com'),
        Usuario(nome='Luciano', email='gabriel@ferreira.com'),
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
