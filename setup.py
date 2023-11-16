# Aqui dentro são criadas as variáveis a serem usadas pelo sistema, além de serem feitos os imports
# e a instalação/atualização de pacotes


# Imports
import pandas as pd
import googlemaps
import json
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
    "farmacia?5", 
    "loterica?5", 
    "escola publica?5", 
    "posto de saude?5"
    ]


# Functions
def concatenate_dataframes(output_name: str):
    concat_glob = glob(f'{path_system}*MATRIX_APPLIED.csv')
    concat_df = pd.read_csv(concat_glob.pop(0), sep=';')
    for cache in track(concat_glob, description=f'Concatenando DataFrames...', style='black', complete_style='white', finished_style='green'):
        new_df = pd.read_csv(cache, sep=';')
        concat_df = pd.concat([concat_df, new_df], axis=0, ignore_index=True)
    concat_df = drop_unnamed(concat_df)
    now = datetime.now().strftime('%d-%m-%Y_%H-%M')
    concat_df.to_csv(f'{path_output}hab_entorno_{now}_{output_name}.csv', sep=';')
    print(f'\n[yellow]CSV {path_output}hab_entorno_{now}_{output_name}.csv successfully created')


def drop_unnamed(df: pd.DataFrame):
    unnamed_list = []
    for unnamed in df.columns:
        if 'Unnamed' in unnamed:
            unnamed_list.append(unnamed)
    df.drop(unnamed_list, axis=1, inplace=True)
    return df


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
