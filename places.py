# Utilizando o nearbyPlaces da biblioteca googlemaps, será percorrida
# a lista de interesse usando como ponto central as coordenadas do local.
# O json retornado é percorrido e as informações desejadas apenas são
# salvas em um dataframe dentro de system/

from setup import *

def nearbyPlaces(hab: str, input_dataframe: pd.DataFrame, row: int, empreendimento: str, cep:str, base: str):
    """
    hab: coordenadas da habitação (no formato ** latitude/longitude **)
    input_dataframe: dataframe original
    row: linha que está sendo processada
    empreendimento: nome do empreendimento que está sendo processado
    cep: cep do empreendimento que está sendo processado
    base: nome do arquivo com diretorio
    """
    size = len(input_dataframe)
    interest_dataframe = pd.DataFrame()
    interest_dataframe[['keyword', 'local_de_interesse', 'coordenada_do_local', 'endereco_do_local', 'tipos_do_local']] = None
    coordinates = hab.split('/')
    for i in interest_zones:
        response = client.places_nearby(
            location=(coordinates[0], coordinates[1]),
            keyword=i.split('?')[0],
            rank_by='distance'
        )
        print(f'Looking for [blue]{i.split("?")[0]}[/blue], [green]got {len(response.get("results"))} results[/green]')
        
        if len(response.get('results')) == 0:
            print('\n[red]No results, looking for next keyword...\n')
        else:
            business = pd.DataFrame(response.get('results'))
            append_dataframe = pd.DataFrame()
            append_dataframe[['keyword', 'local_de_interesse', 'coordenada_do_local', 'endereco_do_local', 'tipos_do_local']] = None
            results = len(response.get('results'))
            print(f'[green1]Processing the [/green1][pink]{i.split("?")[1]}[/pink] [green1]first returned values...[/green1]')
            for ind in business.index:
                if (ind < int(i.split('?')[1])) and (ind < results):
                    append_dataframe.at[ind, 'keyword'] = i.split('?')[0]
                    append_dataframe.at[ind, 'local_de_interesse'] = business.at[ind, 'name']
                    append_dataframe.at[ind, 'coordenada_do_local'] = business.at[ind, 'geometry']['location']
                    append_dataframe.at[ind, 'endereco_do_local'] = business.at[ind, 'vicinity']
                    append_dataframe.at[ind, 'tipos_do_local'] = business.at[ind, 'types']
                    print(f'[magenta]\tAppending items of index[/magenta] {ind}')
            interest_dataframe = pd.concat([interest_dataframe, append_dataframe], axis=0, ignore_index=True)
            print('[green]Successfully processed DataFrame\n')
        
    coordinates = list(map(lambda x: x.replace('.', ','), coordinates))
    interest_columns = interest_dataframe.columns
    original_columns = input_dataframe.columns
    if len(interest_dataframe) == 0:
        print('\n[bright_red]WARNING:[/bright_red] DataFrame of lenght 0\nCSV will not be created, [yellow]txt file with description will be created instead[/yellow]\n')
        error_description = f"Problem: No interest points found\n\nName: {empreendimento}\n\nCoordinates: {'/'.join(coordinates).replace(',', '.')}\n\nVicinity: {input_dataframe.at[row, 'txt_uf']} {input_dataframe.at[row, 'txt_municipio']} {input_dataframe.at[row, 'txt_endereco']}\n\nCEP: {input_dataframe.at[row, 'txt_cep']}\n\nRow/Index at DataFrame: {row}\n\nOrigin DataFrame: {base}"
        problem_handler = open(f'system/PROBLEM_PLACES_at_{empreendimento}.txt', 'w').write(error_description)
    else:
        interest_dataframe[original_columns] = input_dataframe.loc[row]
        interest_dataframe = interest_dataframe[original_columns.tolist()+interest_columns.tolist()]
        print(interest_dataframe)
        print(f'\n[blue]Creating[/blue] CSV for [cyan]{empreendimento}[/cyan]\n')
        df_name = f'{path_system}businessCase&{empreendimento}&{coordinates[0]}+{coordinates[1]}&.csv'
        interest_dataframe = drop_unnamed(interest_dataframe)
        interest_dataframe.to_csv(df_name, sep=';')
        print(f'[yellow]{df_name} created\n\n')
        