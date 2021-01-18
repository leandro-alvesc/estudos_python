# Ler um número inteiro de 4 dígitos (de 1000 a 9999) e imprimir um dígito por linha
num = int(input('Digite um número inteiro de 4 dígitos: '))
linha = ""

if num < 1000 or num > 9999:
    print('Número inválido.')
else:
    for _ in range(4):
        linha += str(num % 10)
        num = int(num / 10)

    for i in range(3, -1, -1):
        print(linha[i])
