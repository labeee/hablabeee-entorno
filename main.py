# Este é o arquivo a ser executado. Nele encontram-se as funções do sistema
# reunidas e devidamente organizadas para sempre funcionar adequadamente sem
# a necessidade de edições ou programação pelo usuário

# Instalador/Atualizador de pacotes
has_setup = open(r'system/has_setup.txt', 'r').read()
if has_setup == '0':
    import os
    os.system('python -m pip install --upgrade pip')
    os.system('pip install --upgrade python')
    os.system('pip install pandas')
    os.system('pip install googlemaps')
    os.system('pip install rich')
    has_setup = open(r'system/has_setup.txt', 'w').write('1')

from setup import *
from places import *
from routes_matrix import *

clear_screen()
print(title)
build_wall(2)

globed = glob(f'{path_input}*.csv')
nbp = False
rm = False

for base in globed:
    input_dataframe = pd.read_csv(base, sep=';')
    opt = 0
    while opt != '':
        print((f'\n\n\n{separators}\nSelect an option to continue:\n\n[1] Apply [blue]NearbyPlaces[/blue]\n[2] Apply [green]RoutesMatrix[/green]\n[3] [yellow]Concatenate[/yellow] and finish process\n\n[ENTER] [red]Exit[/red]\n\n{separators}\n'))
        opt = input('...')
        clear_screen()
        if opt == '1':
            for row in track(input_dataframe.index, description=f'Executando [green]NearbyPlaces...', style='black', complete_style='white', finished_style='green'):
                print(separators)
                empreendimento_nome = input_dataframe.at[row, 'txt_nome_do_empreendimento']
                cep = input_dataframe.at[row, 'txt_cep']
                coordinates = f"{str(input_dataframe.at[row, 'latitude'])}/{str(input_dataframe.at[row, 'longitude'])}"
                print(f'\nApplying NearbySearch to [purple]{empreendimento_nome}[/purple] of coordinates {coordinates}\n')
                nearbyPlaces(hab=coordinates, input_dataframe=input_dataframe, row=row, empreendimento=empreendimento_nome, cep=cep, base=base)
            nbp = True
        elif opt == '2':
            routesMatrix()
            rm = True
        elif opt == '3':
            if not nbp and not rm:
                print(f'[red]WARNING[/red]\n{separators}\nYou seem to not have executed yet both [green]DistanceMatrix[/green]({rm}) and [green]NearbyPlaces[/green]({nbp}),\nare you sure you want to concatenate?\nThis might result in an [red]error[/red]...\n\n[0] Yes\n[ENTER] No\n{separators}\n')
                selection = input('...')
                clear_screen()
                if selection == '0':
                    concat_glob = glob(f'{path_system}*.csv')
                    concat_df = pd.read_csv(concat_glob.pop(0), sep=';')
                    for cache in track(concat_glob, description=f'Concatenando DataFrames...', style='black', complete_style='white', finished_style='green'):
                        new_df = pd.read_csv(cache, sep=';')
                        concat_df = pd.concat([concat_df, new_df], axis=0, ignore_index=True)
                    unnamed_list = []
                    for unnamed in concat_df.columns:
                        if 'Unnamed' in unnamed:
                            unnamed_list.append(unnamed)
                    concat_df.drop(unnamed_list, axis=1, inplace=True)
                    now = datetime.now().strftime('%d-%m-%Y_%H-%M')
                    concat_df.to_csv(f'{path_output}hab_entorno_{now}.csv', sep=';')
                    print(f'\n[yellow]CSV {path_output}hab_entorno_{now} successfully created\n\n')
        
clear_screen()
print(title)
build_wall(5)
print('\nDeveloped by [green]Zac Milioli[/green]\n-\thttps://www.linkedin.com/in/zac-milioli\n-\thttps://github.com/Zac-Milioli\n-\t[yellow][underline]zacmilioli@gmail.com[/underline][/yellow]\n\n')
