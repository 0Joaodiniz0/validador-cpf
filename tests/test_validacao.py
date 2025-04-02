import pytest
from app.validacao import validar_cpf

# Testar se o CPF é válido
def test_validacao_cpf_valido():
    assert validar_cpf("12345678909") == True

# Testar se o CPF é  inválido
def test_validacao_cpf_invalido():
    assert validar_cpf("12345678900") == False

# Testar se o cpf esta vazio
def test_validacao_cpf_vazio():
    assert validar_cpf("") == False

# Testar se tem letras no cpf
def test_validacao_cpf_com_letras():
    assert validar_cpf("12j467nf90g") == False

# Testar se tem digitos iguais no CPF
def test_validacao_cpf_digitos_iguais():
    assert validar_cpf("11111111111") == False

# Testar se CPF esta escrito corretamente
def test_validacao_cpf_formatado():
    assert validar_cpf("123.456.789-09") == True

# Testar se CPF esta com numeros em sequencia
def test_validacao_cpf_numeros_sequenciais():
    assert validar_cpf("12345678900") == False

# Testar se o CPF tem espaços no inicio ou no final
def test_validacao_cpf_espacos():
    assert validar_cpf(" 123.456.789-09 ") == True

# Testar se CPF possui quebra de linha
def test_validacao_cpf_quebra_linha():
    assert validar_cpf("\t123.456.789-09\n") == True

# Testar se o CPF c tem menos de 11 dígitos
def test_validacao_cpf_menos_de_11_digitos():
    assert validar_cpf("123456789") == False

# Testar se o CPF tem mais de 11 dígitos
def test_validacao_cpf_mais_de_11_digitos():
    assert validar_cpf("123456789012") == False
