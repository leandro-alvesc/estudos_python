"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> Meios de comunicação entre os serviços oferecidos por empresas
    (Twitter, Facebook, YouTube) e terceiros (nós devs)

Integrando JSON e Pickle -> pip install jsonpickle

import json

ret = json.dumps(['produto', {'HD Seagate': ('1TB', 'Novo', 250)}])

print(type(ret))

print(ret)

"""
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


bastet = Gato('Bastet', 'Sphynx')

# ret = json.dumps(bastet.__dict__)
# print(ret)

with open('gato.sjon', 'w') as arquivo:
    ret = jsonpickle.encode(bastet)
    arquivo.write(ret)

with open('gato.sjon', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
