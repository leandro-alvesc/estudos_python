"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Pacotes externos oficiais: https://pypi.org

Instalando um módulo: pip install nome_do_modulo

colorama -> utilizado para permitir impressão de textos coloridos no terminal
"""
from colorama import Fore, Back, Style
print(Fore.RED + 'Michael Scott')
print(Fore.GREEN + 'The Office')
print(Fore.CYAN + Style.DIM + 'Dwight Schrute')
print(Style.RESET_ALL)
