# Aqui dentro são criadas as variáveis a serem usadas pelo sistema, além de serem feitos os imports
# e a instalação/atualização de pacotes

# Imports
import pandas as pd
import googlemaps
from places import *
from routes import *

# Paths
path_setup = r'system/has_setup.txt'
path_input = r'input/'
path_output = r'output/'


# Instalador/Atualizador de pacotes
def install_packages():
    has_setup = open(path_setup, 'r').read()
    if has_setup == '0':
        import os
        os.system('python -m pip install --upgrade pip')
        os.system('pip install --upgrade python')
        os.system('pip install pandas')
        os.system('pip install googlemaps')
        has_setup = open(path_setup, 'w').write('1')
