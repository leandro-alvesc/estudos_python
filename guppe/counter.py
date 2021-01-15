"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como
o valor a quantidade de ocorrências desse elemento.


# Utilizando o Counter
from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 9, 0, 9, 90, 90, 'José', 'José', 'Maria']

res = Counter(lista)

print(res)
print(type(res))

# Counter({3: 6, 1: 3, 7: 3, 2: 2, 5: 2, 9: 2, 90: 2, 'José': 2, 4: 1, 6: 1, 0: 1, 'Maria': 1})
# Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
print(Counter('Ana Maria Braga'))

"""
from collections import Counter

# Exemplo 3
texto = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam efficitur sollicitudin aliquet. 
Curabitur nec viverra tortor. Ut eu magna eu enim suscipit pellentesque. 
Curabitur urna lacus, interdum sit amet dui id, bibendum laoreet sem. Vestibulum sagittis rhoncus vestibulum. 
Cras rutrum, sem in feugiat facilisis, augue enim laoreet dolor, in placerat diam justo pretium neque. 
Nullam vitae massa interdum massa placerat cursus. Cras consectetur justo ultrices risus imperdiet, non elementum ante 
dignissim. 
Quisque velit ex, laoreet ac fermentum in, tincidunt ut ipsum. Duis faucibus turpis vel urna mattis, sed molestie eros 
aliquet. 
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In hac habitasse platea dictumst. 
Etiam a venenatis velit.

Donec ante massa, gravida sed enim eu, vehicula hendrerit leo. Nunc dapibus euismod ante nec rutrum. 
Proin gravida lacus eu auctor volutpat. Sed lorem lorem, molestie id lorem sit amet, convallis ullamcorper dui. 
Duis eget varius augue. Nulla volutpat diam felis, ac auctor lorem congue sed. 
Integer accumsan vehicula urna id faucibus. Sed a auctor orci, at scelerisque sem. Etiam lacinia odio sapien, nec v
olutpat massa vehicula ac. 
Morbi iaculis turpis id lacus facilisis fermentum. 
Nullam scelerisque nibh quis ipsum aliquet, in accumsan ipsum sollicitudin. 
Vivamus sit amet hendrerit leo, eu facilisis felis. Suspendisse consectetur libero a orci tincidunt, quis mattis 
tortor ultricies. Nulla facilisi. Mauris placerat efficitur lorem, quis convallis enim ornare sit amet. Curabitur 
nec ante malesuada, scelerisque nibh a, fermentum tellus.
"""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

