# Este é o arquivo a ser executado. Nele encontram-se as funções do sistema
# reunidas e devidamente organizadas para sempre funcionar adequadamente sem
# a necessidade de edições ou programação pelo usuário

# Instalador/Atualizador de pacotes
has_setup = open(r'system/has_setup.txt', 'r').read()
if has_setup == '0':
    import os
    os.system('python -m pip install --upgrade pip')
    os.system('pip install --upgrade python')
    os.system('pip install -r requirements.txt')
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
    name = base.split('\\')[-1]
    input_dataframe = pd.read_csv(base, sep=';', encoding='latin-1')
    opt = 0
    while opt != '':
        print((f'\n\n\n{separators}\nSelect an option to continue:\n\n[1] Apply [blue]NearbyPlaces[/blue]\n[2] Apply [green]RoutesMatrix[/green]\n[3] [yellow]Concatenate[/yellow] and finish process\n\n[ENTER] [bright_red]Exit[/bright_red]\n\n{separators}\n'))
        opt = input('...')
        clear_screen()
        if opt == '1':
            for row in track(input_dataframe.index, description=f'Executando [green]NearbyPlaces...', style='black', complete_style='white', finished_style='green'):
                print(separators)
                empreendimento_nome = input_dataframe.at[row, 'txt_nome_do_empreendimento']
                # cep = input_dataframe.at[row, 'txt_cep']
                coordinates = f"{str(input_dataframe.at[row, 'latitude'])}/{str(input_dataframe.at[row, 'longitude'])}"
                print(f'\nApplying NearbySearch to [purple]{empreendimento_nome}[/purple] of coordinates {coordinates}\n')
                nearbyPlaces(hab=coordinates, input_dataframe=input_dataframe, row=row, empreendimento=empreendimento_nome, base=base)#cep=cep
            nbp = True
        elif opt == '2':
            routesMatrix()
            rm = True
        elif opt == '3':
            if not nbp and not rm:
                print(f'[bright_red]WARNING[/bright_red]\n{separators}\nYou seem to not have executed yet both [green]DistanceMatrix[/green]({rm}) and [green]NearbyPlaces[/green]({nbp}),\nare you sure you want to concatenate?\nConcatenating DataFrames with different columns will result in an [red]error[/red]...\n\n[0] Yes\n[ENTER] No\n{separators}\n')
                selection = input('...')
                clear_screen()
                if selection == '0':
                    concatenate_dataframes(output_name=name)
            else:
                concatenate_dataframes(output_name=name)
        
clear_screen()
print(title)
build_wall(5)
print('\nDeveloped by [bright_green]Zac Milioli[/bright_green]\n-\thttps://www.linkedin.com/in/zac-milioli\n-\thttps://github.com/Zac-Milioli\n-\t[bright_yellow][underline]zacmilioli@gmail.com[/underline][/bright_yellow]\n\n')
