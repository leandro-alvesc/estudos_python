"""
**kwargs

Poderíamos chamar esse parâmetro de **xis mas por convenção chamamos de **kwargs.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')


cores_fav(marcos='verde', julia='amarelo', fernanda='azul')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_fav()
cores_fav(jose='ciano')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'kaori' in kwargs and kwargs['kaori'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Kaori1'
    elif 'kaori' in kwargs:
        return f"{kwargs['kaori']} Kaori!"
    return 'Não sei quem é.'


print(cumprimento_especial())
print(cumprimento_especial(kaori='Oi'))
print(cumprimento_especial(kaori='Python'))
print(cumprimento_especial(sla='oi'))


# Nas nossas funções podemos ter NESSA ORDEM:
 - Parâmetros obrigatórios
 - *args
 - Parâmetros default (não obrigatórios)
 - **kwargs



def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro.')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'José')
minha_funcao(45, 'Kamila', 3, 4, 5, solteiro=False)
minha_funcao(56, 'Antonio', eu='Nao', voce='Vai')
minha_funcao(20, 'Julia', 2, 3, 4, java=False, python=True)

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Kendrick', 'sobrenome': 'Lamar'}

print(mostra_nomes(**nomes))


"""


def soma_tudo(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_tudo(*lista)
soma_tudo(*tupla)
soma_tudo(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_tudo(**dicionario)

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3)  # TypeError
# soma_tudo(**dicionario)


# se na def soma_tudo tiver o parâmetro **kwargs:
# dicionario = dict(a=1, b=2, c=3, nome='Jose')

# soma_tudo(**dicionario, lang='Python')

