"""
Sistema de Arquivos e Navegação

Para utilizar manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System

# getcwd() -> pega o current work directory
print(os.getcwd())

# Para mudar o diretório podemos utilizar o chdir()
os.chdir('..')

print(os.getcwd())

# Checar se o diretório é absoludo ou relativo
print(os.path.isabs('/home/b3lzebuth/'))  # True

print(os.path.isabs('./'))  # False

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (linux e mac), nt (windows)

# Mais detalhes do sistema
print(os.uname())

# Utilizando sys
import sys
print(sys.platform)

# Juntando diretório
print(os.getcwd())  # /home/b3lzebuth/PycharmProjects/estudos_python/guppe

caminho = os.path.join(os.getcwd(), 'exercicios')

os.chdir(caminho)  # /home/b3lzebuth/PycharmProjects/estudos_python/guppe/exercicios

print(os.getcwd())


# Podemos listar os arquivos e diretórios
print(os.listdir())

print(len(os.listdir()))

print(os.listdir('/etc'))
"""
import os

# Podemoss listar com mais detalhes com scandir()

scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))

print(arquivos[0].name)
print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].path)
print(arquivos[0].stat())

# OBS: quando utilizamos scandir() nós precisamos fechá-la
scanner.close()
