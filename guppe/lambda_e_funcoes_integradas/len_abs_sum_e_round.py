"""
Len, Abs, Sum e Round

# Len
len() -> Retorna o tamanho (número de itens) de um iterável
print(len('Kendrick Lamar'))
print(len([1, 2, 3, 4]))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
# Dunder len
print('Kendrick Lamar'.__len__())


# Abs
abs() -> Retorna o valor absoluto de um número inteiro ou real.
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Sum
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos
incluindo o valor inicial

# OBS: valor inicial default = 0
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum({'a': 1, 'b': 2}.values()))


# Round
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada.

"""
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21345321, 2))
print(round(1.21999999, 2))
