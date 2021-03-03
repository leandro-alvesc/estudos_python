"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do código.

1 - SyntaxeError -> Erro de sintaxe, ou seja, escreveu algo que o Python não reconhece como parte da linguagem.
Exemplos:
a)
def funcao:
    print('lala')

b)
None = 1

c)
return


2 - NameError -> Variável ou função não foi definida.
Exemplos:
a)
print(lala)

b)
lala()

c)
a = 8
if a > 10:
    msg = 'É maior que 10'
print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
Exemplos:
a)
print(len(5))

b)
print('a' + [])


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.
Exemplos:
a)
lista = ['lala']
print(lista[6])

b)
print(lista[0][7])


5 - ValueError -> Ocorre quando uma função/operação built-in recebe um argumento com tipo correto mas valor
inapropriado.
Exemplos:
a)
print(int('lala'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
Exemplos:
a)
dic = {}
print(dic['lala'])


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.
Exemplos:
a)
tupla = (11, 2, 31, 4)
print(tupla.sort())


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)
Exemplos:
a)
def nova():
print('lala')

b)
if nova == 5:
print(nova)



OBS: Exceptions e Erros são siinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erros.
"""