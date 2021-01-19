"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom
fazer uma verificação para que a função seja simplificada.

- Já utilizamos várias funções ao decorrer do curso, ex:
    - print()
    - len()
    - input()
    - etc.

"""
"""
# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'vermelho']

# Utilizando uma função integrada (Built-in) do Python
print(cores)

nome = 'Travis Scott'
print(nome)

cores.append('roxo')
# nome.append('lalal')  # AttributeError - O objeto str não possui a função append()

cores.clear()  # Não recebe dados de entrada (parâmetros), como nas outras funções acima.

# DRY - Don't Repeat Yourself (Não repita a si mesmo/seu código)
"""
"""
COMO DEFINIR FUNÇÕES:
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE com letras minúsculas, se for nome composto separar por underline (Snake Case);

parametros_de_entrada -> Opcionais, onde tendo mais de um separar por vírgulas, sendo opcionais ou não;

bloco_da_funcao -> Também chamado de corpo da função, ou implementação. É onde o processamento da função
acontece. Nesse bloco pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def' informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado para
definir blocos
"""
# Definindo uma função:


def diz_oi():
    print('oi!')


"""
OBS: 
1- Veja que dentro das funções podemos utilizar outras funções;
2- Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3- Veja que essa função não recebe nenhum parâmetro de entrada;
4- Veja que essa função não retorna nada.
"""
# Utilizando funções:
diz_oi()

# Exemplo 2:


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


cantar_parabens()

# Em Python podemos inclusive criar uma variável do tipo de uma função e executar essa função através da variável

canta = cantar_parabens

canta()
