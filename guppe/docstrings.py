"""
Documentando Funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a funçãp help()

"""
# Exemplos


def diz_oi(nome=''):
    """Uma função simples que retorna uma string 'Oi!'. Podendo ser informado como parâmetro o nome da pessoa."""
    if len(nome) > 0:
        return f'Oi, {nome}!'
    return 'Oi!'


def exponencial(num, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'num', ou o 'num' à 'potencia' informada.
    :param num: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão = 2
    :return: Retorna o exponencial de 'num' por 'potencia'
    """
    return num ** potencia


print(diz_oi('João'))
print(diz_oi())

print(help(diz_oi))
print(diz_oi.__doc__)

print(help(exponencial))
print(exponencial.__doc__)
