# Este é o arquivo a ser executado. Nele encontram-se as funções do sistema
# reunidas e devidamente organizadas para sempre funcionar adequadamente sem
# a necessidade de edições ou programação pelo usuário

from setup import *
install_packages()

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
        print(separators)
        print((f'\nSelect an option to continue:\n\n[1] Apply [blue]NearbyPlaces[/blue]\n[2] Apply [green]RoutesMatrix[/green]\n[3] [yellow]Concatenate[/yellow] and finish process\n\n[ENTER] [red]Exit[/red]\n\n{separators}\n'))
        opt = input('...')
        clear_screen()
        if opt == '1':
            for row in track(input_dataframe.index, description=f'Executando [green]NearbyPlaces...', style='black', complete_style='white', finished_style='green'):
                empreendimento_nome = input_dataframe.at[row, 'txt_nome_do_empreendimento']
                cep = input_dataframe.at[row, 'txt_cep']
                coordinates = f"{str(input_dataframe.at[row, 'latitude']).replace(',', '.').replace('°', '')}/{str(input_dataframe.at[row, 'longitude']).replace(',', '.').replace('°', '')}"
                nearbyPlaces(rad=radius, limit=itens_limit, hab=coordinates, input_dataframe=input_dataframe, row=row, empreendimento=empreendimento_nome, cep=cep)
            nbp = True
            clear_screen()
        elif opt == '2':
            routesMatrix()
            rm = True
            clear_screen()
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
                    now = datetime.now().strftime('%d-%m-%Y_%H-%M')
                    concat_df.to_csv(f'{path_output}hab_entorno_{now}.csv', sep=';')
            clear_screen()
        
clear_screen()
print(title)
build_wall(5)
print('\nDeveloped by [green]Zac Milioli[/green]\n-\thttps://www.linkedin.com/in/zac-milioli\n-\thttps://github.com/Zac-Milioli\n-\t[yellow][underline]zacmilioli@gmail.com[/underline][/yellow]\n\n')
