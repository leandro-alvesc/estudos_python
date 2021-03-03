"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo que o programa
pare de funcionar o usuário receba mensagens de erro inesperadas.

A forma geral mais simples:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de probelmas


# Exemplo 1 - Tratando um erro genérico
try:
    lala()
except:
    print('Erro')


OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erro. O ideal é sempre tratar de forma
específica.

# Exemplo 2 - Tratando um erro específico
try:
    lala()
except NameError:
    print('Usando uma função inexistente.')

# Exemplo 3 - Tratando um erro específico com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 4 - Podemos efetuar diversos tratamentos de erros de uma vez
try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "gilberto"}

print(pega_valor(dic, "nome"))
print(pega_valor(dic, "game"))
print(pega_valor(7, "nome"))
