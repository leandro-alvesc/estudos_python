"""
Estruturas Condicionais
if, else, elif (else if)

# Estrutura condicional if, else em C
if(idade < 18) {
    printf("Menor de idade.");
} else if(idade == 18) {
    printf("Tem 18 anos.");
} else {
    printf("Menor de idade.")
}

# Estrutura condicional if, else em Java
if(idade < 18) {
    System.out.println("Menor de idade.");
} else if(idade == 18) {
    System.out.println("Tem 18 anos.");
} else {
    System.out.println("Menor de idade")
}
"""

idade = 18

if idade < 18:
    print('Menor de idade.')
elif idade == 18:
    print('Tem 18 anos.')
else:
    print('Maior de idade')
