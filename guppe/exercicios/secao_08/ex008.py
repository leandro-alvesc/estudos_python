# Função q receba catetos a e b e calcule a hipotenusa


def hipotenusa(a, b):
    hip = (a ** 2 + b ** 2) * (1/2)
    return hip


cat_a = float(input('Cateto a: '))
cat_b = float(input('Cateto b: '))

print(f'Hipotenusa: {hipotenusa(cat_a, cat_b)}')
