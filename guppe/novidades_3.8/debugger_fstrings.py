def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.31, 4.23)

print(f'O resultado é {resultado}')
print(f'O resultado é {multiplicar(3.2, 56.3):.2f}')

nome: str = 'Teste'

print(f"nome='{nome}'")
print(f'{nome=}')

print(f'{nome.upper()[::-1] = }')
