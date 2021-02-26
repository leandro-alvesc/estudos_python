"""
Decorators com diferentes assinaturas

- Padrão: Decorator Pattern (*args, **kwargs)

- Assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

# Relembrando


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def ola(nome):
    return f'Olá, meu nome é {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, gostaria de {principal}, acompanhado de {acompanhamento} por favor.'


@gritar
def palavras(*args):
    total = ""
    for palavra in args:
        total += palavra
        total += " "
    return total


# Teste
print(ola('Bruno'))

print(ordenar('Ovo', 'Batata Frita'))

print(palavras('Oi', 'Olá', 'Batata', 'Baseball'))
"""
# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def valida(*args, **kwargs):
            if args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return valida
    return interna


@verifica_primeiro_argumento('belinha')
def nome_pet(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_10(n1, n2):
    return n1 + n2


print(soma_10(10, 20))

print(nome_pet('belinha', 'renato'))
