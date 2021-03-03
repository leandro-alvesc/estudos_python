"""
Recebendo dados do Usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simpels triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Leandro Alves'
- Aspas duplas -> "Leandro Alves"
- Aspas simpels triplas -> '''Leandro Alves'''
"""
# - Aspas duplas triplas -> """ Leandro Alves """

# Entrada de dados
nome = input('Qual seu nome? ')
# print("Qual seu nome? ")
# nome = input()  # Input -> Entrada

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a), %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')

idade = int(input('Qual sua idade? '))

# print("Qual a sua idade? ")
# idade = input()

# Processamento

# Saída de dados

# Exemplo de print 'antigo' 2.x
# print('Seu nome é %s e você tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('Seu nome é {0} e você tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'Seu nome é {nome} e você tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'{nome} nasceu em {2020 - idade}')
