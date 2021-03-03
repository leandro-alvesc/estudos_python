"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:
TODA ENTRADA DEVE SER TRATADA!
OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')


# Finally -> É sempre executado, independente se houve exceção ou não
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor inválido')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# OBS: O finally é geralmente utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo - Pythônico
# OBS: Você é responsável pela entrada das suas funções


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Impossível dividir por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))


# Exemplo mais complexo - Semi-Genérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return 'Ocorreu um erro: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
"""
