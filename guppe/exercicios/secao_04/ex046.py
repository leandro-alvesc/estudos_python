# Ler um número inteiro positivo de 3 dígitos (de 100 a 999). Gerar um outro com os números invertidos
num = int(input('Digite um número positivo de 3 dígitos: '))
inv = ""

if num < 100 or num > 999:
    print('Número inválido')
else:
    for _ in range(3):
        inv += str(num % 10)
        num = int(num / 10)

print(inv)
