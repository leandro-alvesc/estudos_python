# Criando a própria versão de loop


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


lista = [1, 2, 3, 4]
meu_for(lista)
print()
meu_for('teste')
