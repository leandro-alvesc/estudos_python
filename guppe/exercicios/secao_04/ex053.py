# Ler as dimensões de um terreno e o preço do metro de tela. Imprimir o custo para cercar esse terreno com tela
comp = float(input('Digite o comprimento do terreno: '))
larg = float(input('Digite a largura do terreno: '))
prec = float(input('Digite o preço do metro de tela: R$ '))

custo = (comp * 2 + larg * 2) * prec

print(f'Será gasto R$ {custo:.2f} para cercar o terreno.')
