# Receber dois números:
# 1- calcular a soma dos numeros pares desse intervalo de numeros, incluindo os digitados
# 2- multiplicacao dos numeros ímpares desse intervalo incluindo os digitados
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma_par = 0
multi_impar = 1

if a > b:
    for n in range(b, a+1):
        if n % 2 == 0:
            soma_par += n
        else:
            multi_impar *= n
else:
    for n in range(a, b+1):
        if n % 2 == 0:
            soma_par += n
        else:
            multi_impar *= n

print(f'Soma dos pares: {soma_par}')
print(f'Multiplicação dos ímapres: {multi_impar}')
