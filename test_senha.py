from senha import senha_valida


def test_senha_com_exatamente_14_caracteres_e_aceita():
    # preparar
    senha = "a" * 14
    # agir
    resultado = senha_valida(senha)
    # verificar
    assert resultado is True


def test_senha_com_13_caracteres_e_rejeitada():
    # preparar
    senha = "a" * 13
    # agir
    resultado = senha_valida(senha)
    # verificar
    assert resultado is False


def test_senha_vazia_e_rejeitada():
    # preparar
    senha = ""
    # agir
    resultado = senha_valida(senha)
    # verificar
    assert resultado is False


def test_senha_so_com_espacos_e_rejeitada():
    # preparar
    senha = " " * 16
    # agir
    resultado = senha_valida(senha)
    # verificar
    assert resultado is False
