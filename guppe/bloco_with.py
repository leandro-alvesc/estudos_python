"""
Bloco With - Forma Pythônica de manipular arquivos

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após
o bloco.

"""
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# print(arquivo.read())  # ValueError

print(arquivo.closed)
