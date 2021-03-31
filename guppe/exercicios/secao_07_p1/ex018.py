# Ler um vetor de 10 numeros, ler um numero x, conte os multiplos do numero x num vetor e mostre-os na tela
vetor = [int(input(f'Digite o número {v+1}: ')) for v in range(10)]

x = int(input('Digite o número para verificar os múltiplos: '))

novo_vetor = []
for n in vetor:
    if n % x == 0:
        novo_vetor.append(n)

print(novo_vetor)
