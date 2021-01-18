# Calcular o ano de nascimento a partir da idade e ano atual
ano_atual = int(input('Em que anos estamos? '))
idade = int(input('Qual a sua idade? '))

ano_nasc = ano_atual - idade

print(f'Você nasceu em: {ano_nasc}')
