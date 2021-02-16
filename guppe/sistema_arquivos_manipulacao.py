"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('texto.txt'))  # True
print(os.path.exists('lalala.txt'))  # False

# Diretório - path relativo
print(os.path.exists('pacote_teste'))  # True
print(os.path.exists('pacote_teste/pacote_teste_2'))  # True
print(os.path.exists('pacote_teste/lala.py'))  # False

# Diretório - path absoluto
print(os.path.exists('/home/'))  # True
print(os.path.exists('/home/user/lala'))  # False


# Criando arquivos

# Forma 1
open('arquivo.txt', 'w').close()

# Forma 2
open('arquivo.txt', 'a').close()

# Forma 3
with open('arquivo.txt', 'w') as arquivo:
    pass

# Forma 4 - RECOMENDADA

os.mknod('arquivo.txt')
os.mknod('/home/user/arquivo.txt')

# OBS: No MacOS pode haver PermissionError
# OBS: Se o arquivo ja existir, dará FileExistsError


# Criando diretórios - únicos
os.mkdir('templates')
os.mkdir('/home/user/templates')

# OBS: Se já existir teremos FileExistsError
# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError

# Criando diretórios - múltiplos
os.makedirs('templates/lala/lala2')  # Se já existir teremos FileExistsError
os.makedirs('templates/lala/lala2', exist_ok=True)  # Se existir, ignora

# Renomeando Diretórios e Arquivos
os.rename('templates/lala/lala2', 'templates/lala/teste')
os.rename('templates/lala/teste/arquivo.txt', 'templates/lala/teste/renomear.txt')


# Removendo arquivos
# ATENÇÃO: Ao deletar com comandos de deleção, eles não vão para a lixeira, eles somem.
os.remove('texto.txt')

# OBS: No Windows, se o arquivo estiver em uso dará erro.
# OBS: Caso não exista: FileNotFoundError
# OBS: Se informar diretório em vez de arquivo: IsADirectoryError

# Removendo diretórios vazios
os.rmdir('templates')
# OBS: Se o diretório tiver conteúdo: OSError
# OBS: Se o diretório não existir: FileNotFoundError

# Removendo todos os arquivos em um diretório
for arquivo in os.scandir('templates'):
    if arquivo.is_file():
        os.remove(arquivo)

# Remover diretórios vazios
os.removedirs('templates/teste')

# Biblioteca send2trash
pip install send2trash
sudo apt-get install lsb-core  # -> se der erro na instalação

from send2trash import send2trash
send2trash('arquivo.txt')  # Vai para a lixeira
send2trash('teste')  # Podendo informar diretórios

# Trabalhando com diretórios e arquivos temporários
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Diretório temporário: {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporário.txt'), 'w') as arquivo:
        arquivo.write('Teste\n')
    input()  # Para o programa segurar o arquivo, já que quando sair do with ele deleta

# OBS: Possivelmente o código não funciona em sistema Windows, pela forma diferente de trabalhar com arquivos
# temporários

# Trabalhando somente com arquivos temporários
import tempfile
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'teste')  # Transformando em bits para usar arquivo temporário
    tmp.seek(0)
    print(tmp.read())

"""
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'teste\n')

print(arquivo.name)
arquivo.seek(0)
print(arquivo.read())

input()

arquivo.close()
