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
    for caso in globed:
        df = pd.read_csv(caso, sep=';')
        coord = caso.split('?')[2]
        pin_point = {'lat': coord[0], 'lng': coord[1]}
        coord_destinations = []
        for i in df.index:
            coord_destinations.append(df.at[i, 'coordenada_interesse'])
        response = client.distance_matrix(
            origins=pin_point,
            destinations=coord_destinations,
            mode='walking'
        )
        
