# Ler 6 valores inteiros pares e mostrar na ordem inversa
vetor = []

for _ in range(6):
    valor = int(input('Entre um valor par: '))
    while valor % 2 != 0:
        print('Valor inválido')
        valor = int(input('Entre um valor par: '))
    vetor.append(valor)

vetor.reverse()
print(vetor)
