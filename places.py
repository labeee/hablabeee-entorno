# Utilizando o nearbyPlaces da biblioteca googlemaps, será percorrida
# a lista de interesse usando como ponto central as coordenadas do local.
# O json retornado é percorrido e as informações desejadas apenas são
# salvas em um dataframe dentro de system/

from setup import *

def nearbyPlaces(hab: str, input_dataframe: pd.DataFrame, row: int, empreendimento: str, cep:str):
    """
    hab: coordenadas da habitação (no formato ** latitude/longitude **)
    input_dataframe: dataframe original
    row: linha que está sendo processada
    empreendimento: nome do empreendimento que está sendo processado
    cep: cep do empreendimento que está sendo processado
    """
    size = len(input_dataframe)
    interest_dataframe = pd.Dataframe()
    interest_dataframe[['local_de_interesse', 'coordenada_do_local', 'endereco_do_local', 'tipos_do_local']] = None
    coordinates = hab.split('/')
    for i in interest_zones:
        response = client.places_nearby(
            location=(coordinates[0], coordinates[1]),
            keyword=i.split('?')[0],
            rank_by='distance'
        )
        business = pd.DataFrame(response.get('results'))

        append_dataframe = pd.DataFrame()
        append_dataframe[['local_de_interesse', 'coordenada_do_local', 'endereco_do_local', 'tipos_do_local']] = None
        counter = 0
        while counter < int(i.split('?')[1]):
            for ind in business.index:
                append_dataframe.at[ind, 'local_de_interesse'] = business.at[ind, 'name']
                append_dataframe.at[ind, 'coordenada_do_local'] = business.at[ind, 'geometry']['location']
                append_dataframe.at[ind, 'endereco_do_local'] = business.at[ind, 'vicinity']
                append_dataframe.at[ind, 'tipos_do_local'] = business.at[ind, 'types']
                counter += 1
        interest_dataframe = interest_dataframe.append(append_dataframe, ignore_index=True)
        
    interest_columns = interest_dataframe.columns
    original_columns = input_dataframe.columns
    interest_dataframe[original_columns] = input_dataframe.loc[row]
    interest_dataframe = interest_dataframe[original_columns.tolist()+interest_columns.tolist()]
    interest_dataframe.to_csv(f'{path_output}businessCase?{empreendimento}?{hab}?.csv', sep=';')
