# Este é o arquivo a ser executado. Nele encontram-se as funções do sistema
# reunidas e devidamente organizadas para sempre funcionar adequadamente sem
# a necessidade de edições ou programação pelo usuário

from setup import *
install_packages()

clear_screen()
print(title)
build_wall(2)

globed = glob(f'{path_input}*.csv')

for base in globed:
    input_dataframe = pd.read_csv(base, sep=';')
    print(f'\n\t- Scanned {base}\n')
    print(separators)
    opt = 0
    while opt != '':
        opt = input(f'\nSelect an option to continue:\n\n[1] Apply NearbyPlaces\n[2] Apply RoutesMatrix\n\n[ENTER] Exit\n\n{separators}\n...')
        clear_screen()
        if opt == '1':
            for row in input_dataframe.index:
                empreendimento_nome = input_dataframe.at[row, 'txt_nome_do_empreendimento']
                cep = input_dataframe.at[row, 'txt_cep']
                coordinates = f"{str(input_dataframe.at[row, 'Latitude']).replace(',', '.').replace('°', '')}/{str(input_dataframe.at[row, 'Longitude']).replace(',', '.').replace('°', '')}"
                nearbyPlaces(rad=radius, limit=itens_limit, hab=coordinates, input_dataframe=input_dataframe, row=row, empreendimento=empreendimento_nome, cep=cep)
        elif opt == '2':
            routesMatrix()
        
clear_screen()
print(title)
build_wall(5)
