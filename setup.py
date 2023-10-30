# Aqui dentro são criadas as variáveis a serem usadas pelo sistema, além de serem feitos os imports
# e a instalação/atualização de pacotes


# Imports
import pandas as pd
import googlemaps
from glob import glob
from places import *
from routes import *


# API Params
key = open(path_key, 'r').read()
client = googlemaps.Client(key)


# Paths
path_setup = r'system/has_setup.txt'
path_input = r'input/'
path_output = r'output/'
path_key = r'system/api_key.txt'


# Variables
interest_zones = [
    "mercado", 
    "farmácia", 
    "lotérica", 
    "escola pública", 
    "posto de saúde"
    ]

# limit = 8
# radius = 200


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


# ASCII ART/CONFIGS

title = """\n█▀▀ █▄░█ ▀█▀ █▀█ █▀█ █▄░█ █▀█   ▄▄   █░█ ▄▀█ █▄▄ █░░ ▄▀█ █▄▄ █▀▀ █▀▀ █▀▀
██▄ █░▀█ ░█░ █▄█ █▀▄ █░▀█ █▄█   ░░   █▀█ █▀█ █▄█ █▄▄ █▀█ █▄█ ██▄ ██▄ ██▄"""

wall = """_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__\n"""
wall_top = '______________________________________________________________________'
def build_wall(height: int):
    print(f'{wall_top}\n{wall*height}\n')

clean = '\n'*50
def clear_screen():
    print(clean)

separators = '>'*50
