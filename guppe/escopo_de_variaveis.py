"""
Escopo de Variáveis

Dois casos de escopo:
1- Variáveis globais;
    - Seu escopo compreende todo o programa.
2- Variáveis locais;
    - Seu escopo está limitado ao bloco onde foi declarada.

Para declarar variável em Python, fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica, ou seja, ao declararmos uma variável não colocamos o tipo de
dado dela. Esse tipo é inferido ao atribuírmos o valor.

Exemplo em C:
int numero = 42;

Exemplo em Python:
numero = 42
numero = '42' # Em Python permite reatribuição
"""
numero = 42  # exemplo de variável global
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada dentro do bloco, portanto é local
    print(novo)
