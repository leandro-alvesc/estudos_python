def diz_oi(nome: str) -> str:
    return f'Olá, {nome}'


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


# Pode ser feito a definição de tipos nos comentários
def cabecalho2(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


def cabecalho3(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho(diz_oi('Gustavo')))
print(cabecalho(diz_oi('Gustavo'), alinhamento=False))

print(cabecalho.__annotations__)
