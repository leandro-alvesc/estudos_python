# pip install mypy
# mypy nome_do_arquivo.py
def diz_oi(nome: str) -> str:
    return f'Olá, {nome}'


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho(diz_oi('Gustavo')))
print(cabecalho(diz_oi('Gustavo'), alinhamento=False))

# print(cabecalho(diz_oi('Gustavo'), alinhamento='False'))
