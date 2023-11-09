# Aqui dentro são criadas as variáveis a serem usadas pelo sistema, além de serem feitos os imports
# e a instalação/atualização de pacotes


# Imports
import pandas as pd
import googlemaps
from glob import glob
from rich.progress import track
from rich.traceback import install
from rich import print
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
install()


# Paths
path_system = r'system/'
path_input = r'input/'
path_output = r'output/'
path_key = f'{path_system}api_key.txt'


# API Params
key = open(path_key, 'r').read()
client = googlemaps.Client(key)


# Variables
interest_zones = [
    "mercado?5", 
    "farmácia?5", 
    "lotérica?5", 
    "escola pública?5", 
    "posto de saúde?5"
    ]


# ASCII ART/CONFIGS

title = """\n█▀▀ █▄░█ ▀█▀ █▀█ █▀█ █▄░█ █▀█   ▄▄   █░█ ▄▀█ █▄▄ █░░ ▄▀█ █▄▄ █▀▀ █▀▀ █▀▀
██▄ █░▀█ ░█░ █▄█ █▀▄ █░▀█ █▄█   ░░   █▀█ █▀█ █▄█ █▄▄ █▀█ █▄█ ██▄ ██▄ ██▄"""

wall = """_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__\n"""

wall_top = '______________________________________________________________________'

def build_wall(height: int):
    print(f'[orange1]{wall_top}\n{wall*height}\n')

clean = '\n'*50
def clear_screen():
    print(clean)

separators = '>'*50
