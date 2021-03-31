# Faça um vetor de tamanho 50 preenchido com (i+5*i)%(i+1), sendo i a posiçao do elemento do vetor
vetor = [((i+5*i) % (i+1)) for i in range(50)]

print(vetor)
