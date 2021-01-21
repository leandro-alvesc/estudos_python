# Ler uma sequencia de numeros interios e determinar se sao pares ou nao. Deversá ser informado o número de dados lidos
# e quantos deles são pares. Termina quando digitado o valor 1000
num = None
par = 0
tot = 0
while num != 1000:
    print('Digite 1000 para sair.')
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0 and num != 1000:
        par += 1
        tot += 1
    elif num != 1000:
        tot += 1

print(f'Total de pares: {par}. \nTotal de números: {tot}')
