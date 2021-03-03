"""
Loop While

Forma geral

while expressao_booleana:
    //execução do loop

O bloco while será repetido enquanto a expressão for verdadeira.

# Exemplo 1
numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while precisamos cuidar do critério de parada para não causar um loop infinito

# Exemplo 2

"""
resposta = ' '

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

print("Saindo...")