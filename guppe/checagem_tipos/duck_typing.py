class Livro:

    def __len__(self):
        return 42


livro = Livro()
nome = 'Ola tudo bem'
lista = [1, 2, 3, 4]
dicio = {"a": 1, "b": 2, "c": 3}

print(len(livro))
print(len(nome))
print(len(lista))
print(len(dicio))

# Se determinado objeto se comporta igual, então ele terá métodos similares
