# Aqui é executada a função distance matrix da biblioteca googlemaps
# usando como origem as coordenadas do local buscado, e como destinos
# todos os retornos da função nearbyPlaces registrados no dataframe.
# O json retornado é percorrido e as informações desejadas são registradas
# junto ao dataframe.

from setup import *

def routesMatrix():
    globed = glob(f'{path_system}*.csv')
    print(separators)
    print(f'\n\t - Starting distance matrix search')
    print(separators)
    for caso in track(globed, description='Aplicando [green]DistanceMatrix...', style='black', complete_style='white', finished_style='green'):
        df = pd.read_csv(caso, sep=';')
        coord = caso.split('?')[2]
        pin_point = {'lat': coord[0], 'lng': coord[1]}
        coord_destinations = []
        for i in df.index:
            coord_destinations.append(df.at[i, 'coordenada_interesse'])
        response = client.distance_matrix(
            origins=pin_point,
            destinations=coord_destinations,
            mode='walking',
            language='pt-BR',
            units='metric',
            transit_routing_preference='less_walking'
        )
        
        rows = response.get('rows')[0].get('elements')
        df_response = pd.DataFrame(rows)
        df_response.drop(columns=['status'], axis=1, inplace=True)

        for i in df_response.index:
            df_response.at[i, 'distance'] = df_response.at[i, 'distance'].get('value')
            df_response.at[i, 'duration'] = df_response.at[i, 'duration'].get('value')
        df_response.columns = ['distance(meters)', 'duration(seconds)']

        df_response = pd.concat([df, df_response], ignore_index=True, axis=1)
        df_response.to_csv(caso, sep=';')
