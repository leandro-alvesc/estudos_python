"""
Pacotes
É um diretório contendo uma coleção de módulos

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões 3.x do Python, não é mais obritarória a utilização desse arquivo, mas normalmente ainda é utilizado
para manter compatibilidade.

from pacote_teste import teste1, teste2

from pacote_teste.pacote_teste_2 import  teste3, teste4

print(teste1.pi)
print(teste1.funcao1(1, 5))

print(teste2.curso)
print(teste2.funcao2())

print(teste3.funcao3())

print(teste4.funcao4())

"""
from pacote_teste.teste1 import funcao1

print(funcao1(5, 5))
