"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java:
for(int i = 1; i < 10; i++){
    //bloco
}

Python:
for item in iteravel:
   //loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Segunda feira'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
    OBS: range(valor_inicial, valor_final)
         o valor final nao é inclusive

nome = 'Carlos Alberto'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

for letra in nome:
    print(letra, end='')

# Exemplo de for 2 (iterando sobre uma lista
for numero in lista:
    print(numero)


# Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)


# Exemplo Enumerate
Enumerate:
    ((0, 'C'), (1, 'a'), (2, 'r'), (3, 'l'), (4, 'o')...)

for i, v in enumerate(nome):
    print(nome[i])

for i, v in enumerate(nome):
    print(v)

for _, v in enumerate(nome):  # _ serve para descartar um valor que não precisamos
    print(v)

for valor in enumerate(nome):
    print(valor)  # valor[0] - somente os indices; valor[1] - somente as letras


# Exemplo de loop + soma
qnt = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qnt + 1):
    num = int(input(f'Informe o número {n}/{qnt}: '))
    soma += num
print(f'A soma é {soma}.')

--------------------------------------------------------
Tabela de Emojis Unicode: https:\\apps.timwhitlock.info/emoji/tables/unicode

"""
# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
