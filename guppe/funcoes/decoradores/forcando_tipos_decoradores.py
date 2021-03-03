"""
Forçando tipos de dados com decoradores

"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Oi'), int('3')
            return funcao(*novo_args)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Oi', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('10', 5)
