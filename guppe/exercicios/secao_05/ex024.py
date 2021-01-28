"""
Uma empresa vende o mesmo produto para quatro diferentes estados
Cada estado possui uma taxa de imposto diferente
MG 7%, SP 12%, RJ 15%, MS 8%

Entrar um valor e o estado destino do produto e retornar o preço final acrescido do imposto
Se o estado não for válido mostrar erro
"""
valor = float(input('Digite o valor do produto: '))
estado = input('Digite o estado (MG, SP, RJ ou MS): ')
total = 0

if estado == 'MG':
    total = valor + valor * 0.07
elif estado == 'SP':
    total = valor + valor * 0.12
elif estado == 'RJ':
    total = valor + valor * 0.15
elif estado == 'MS':
    total = valor + valor * 0.08
else:
    print('Estado Inválido')

print(f'O valor do produto para {estado} é R$ {total}.')
