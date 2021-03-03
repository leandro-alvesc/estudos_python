"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Para and: ambos precisam retornar True para o resultado ser verdadeiro
Para or: um dos dois precisam retornar True para o resultado ser verdadeiro
Para not: o valor do booleano é invertido, True -> False e False -> True
Para is: o valor é comparado com um segundo valor
"""
ativo = False
logado = True

if ativo and logado:
    print('Bem vindo usuário!')
elif not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu email.')
elif not logado:
    print('Por favor, efetue o Login')

# ativo é False?
print(ativo is False)
