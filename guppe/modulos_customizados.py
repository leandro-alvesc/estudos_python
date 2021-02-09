"""
Módulos Customizados

Como módulos Python nada mais são que arquivos Python, todos os arquivos que criamos são módulos prontos para serem
utilizados

# Importando uma função específica do nosso módulo
from funcoes_com_parametros import nome_completo

print(nome_completo('Jose', 'Silva'))

# Importando o módulo inteiro
import funcoes_com_parametros as fcp

print(fcp.sobrenome)
print(fcp.nome)

"""
from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
