# Aqui é executada a função distance matrix da biblioteca googlemaps
# usando como origem as coordenadas do local buscado, e como destinos
# todos os retornos da função nearbyPlaces registrados no dataframe.
# O json retornado é percorrido e as informações desejadas são registradas
# junto ao dataframe.

from setup import *

def routesMatrix():
    globed = glob(f'{path_system}*.csv')
    for caso in track(globed, description='Aplicando [green]DistanceMatrix...', style='black', complete_style='white', finished_style='green'):
        print(separators)
        df = pd.read_csv(caso, sep=';')
        coord = caso.split('&')[2]
        coord = coord.split('+')
        pin_point = {'lat': coord[0].replace(',', '.'), 'lng': coord[1].replace(',', '.')}
        coord_destinations = []
        for i in df.index:
            json_format = df.at[i, 'coordenada_do_local'].replace("'", "\"")
            json_format = json.loads(json_format)
            coord_destinations.append(json_format)
        print(f'Searching [green]Matrix[/green] for [yellow]{caso}[/yellow] with coordinates {pin_point}\n')
        response = client.distance_matrix(
            origins=pin_point,
            destinations=coord_destinations,
            mode='walking',
            language='pt-BR',
            units='metric'
        )
        
        rows = response.get('rows')[0].get('elements')
        print(f'[purple]Returned[/purple]:\n{response}\n')
        df_response = pd.DataFrame(rows)
        df_response.drop(columns=['status'], axis=1, inplace=True)

        for i in df_response.index:
            minutos = int(df_response.at[i, 'duration'].get('value')) / 60
            df_response.at[i, 'distance'] = df_response.at[i, 'distance'].get('value')
            df_response.at[i, 'duration'] = round(minutos, 2)
        df_response.columns = ['distancia(metros)', 'tempo_de_viagem(minutos)']
        print(f'DataFrame from response:\n{df_response}\n\n')

        df_response = pd.concat([df, df_response], axis=1)
        print(f'DataFrame concatenated:\n{df_response}\n\n')
        print(f'\n[green]Creating[/green] CSV for [yellow]{caso}[/yellow]\n\n')
        df_response.to_csv(caso, sep=';')
