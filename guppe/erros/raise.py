"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: Não é uma função, é uma palavra reservada.
OBS: O raise assim como return, finaliza a função.

Para simplificar, é útil para criar nossas próprias exceções e mensagens de erro.

Forma de utilização:
raise TipoDoErro('Mensagem de erro')
"""
# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor presia ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Lala', 'rosa')
