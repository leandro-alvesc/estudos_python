"""
Tipo Booleano

Vem da Álgebra Booleana, por George Boole

Verdadeiro -> True
Falso -> False
"""
ativo = True

print(ativo)

# Operações básicas:
#   Negação (not):
#       Fazendo a negação, o valor irá retornar o oposto
print('\n---- negação (not) ----')
print(not ativo)

#   Ou (or):
#       É uma operação binária, depende de dois valores. Ou um ou outro deve ser verdadeiro.
print('\n---- ou (or) ----')
print(True or False)

#   E (and):
#       Também é uma operação binária. Ambos os valores devem ser verdadeiros.
print('\n---- e (and) ----')
print(True and True)
print(True and False)
