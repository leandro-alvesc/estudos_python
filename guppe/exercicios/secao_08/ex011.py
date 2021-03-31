# Receber 3 notas como parâmetro e uma letra (A - média aritmética, P - média ponderada, pesos 5, 3, 2)
def media(n1, n2, n3, opcao):
    if opcao == 'A':
        media_a = (n1 + n2 + n3) / 3
        return f'{media_a:.2f}'
    elif opcao == 'P':
        media_p = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / (5 + 3 + 2)
        return f'{media_p:.2f}'
    else:
        return 'Opção inválida.'


m1 = media(8, 7.8, 9, 'A')
print(m1)
