"""
Conjuntos

- Em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- Em Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índices: conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a
ordenação deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (Set) e mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem apresentar erro.

# Forma 2 (mais comum)
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# É possível transformar listas/tuplas em sets
lista = [1, 2, 3, 4, 4, 5, 5, 6]
s = set(lista)
print(s)

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Encontrei o 3')
else:
    print('Não encontrei o 3')


# Importante lembrar que além de não termos valores duplicados, não temos ordem
# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos.')

# Tuplas aceitam valores duplicados
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos.')

# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como tod0 outro conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)



# Usos interessantes com sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Fortaleza', 'Cuiaba', 'Campo Grande', 'São Paulo']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

print(len(set(cidades)))


# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. É ignorado.
print(s)


# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é índice, informamos o valor a ser removido. Nenhum valor é retornado.
print(s)
# OBS: Caso o valor não seja encontrado será gerado KeyError

# Forma 2
s.discard(2)
print(s)
# OBS: Se o valor não for encontrado nenhum erro é gerado.


# Copiando um conjunto para outro
s = {1, 2, 3}

# Forma 1 - Deep Copy
novo = s.copy()
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)


# Podemos remover todos os itens de um conjunto
s.clear()
print(s)


# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos:
#    - Estudantes do curso Python
#    - Estudantes do curso Java

estudantes_python = {'Marcos', 'Patrícia', 'Pedro', 'José', 'Lilian', 'Gustavo'}
estudantes_java = {'Fernando', 'Roberta', 'José', 'Ana', 'Patrícia'}

# Veja que alguns alunos que estudam Python também estudam Java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |
unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - utilizando intersection
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - utilizando o &
ambos2 = estudantes_java & estudantes_python
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)



"""
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
