# Utilizando o nearbyPlaces da biblioteca googlemaps, será percorrida
# a lista de interesse usando como ponto central as coordenadas do local.
# O json retornado é percorrido e as informações desejadas apenas são
# salvas em um dataframe dentro de system/

from setup import *

def nearbyPlaces(radius: int, limit: int, hab: str, input_dataframe: pd.DataFrame, row: int, empreendimento: str, cep:str):
    """
    radius: raio, em metros, de busca
    limit: tamanho limite de itens encontrados para parar a busca
    hab: coordenadas da habitação (no formato ** latitude/longitude **)
    input_dataframe: dataframe original
    row: linha que está sendo processada
    empreendimento: nome do empreendimento que está sendo processado
    cep: cep do empreendimento que está sendo processado
    """
    interest_dataframe = pd.Dataframe()
    interest_dataframe[['ponto_interesse', 'coordenada_interesse', 'endereco_interesse', 'tipo_interesse']] = None
    coordinates = hab.split('/')
    found_list = []
    print(f'\n\t- Created DataFrame for interest points')
    while len(found_list) < limit:
        for i in interest_zones:
            print(f'\n\t- Requesting nearby {i}')
            response = client.places_nearby(
                location=(coordinates[0], coordinates[1]),
                keyword=i,
                # rank_by='distance'
                radius=radius
            )
            business = pd.DataFrame(response.get('results'))
            print(f'\n\t- Found {len(business)} results: \n{business}\n')

            append_dataframe = pd.DataFrame()
            append_dataframe[['ponto_interesse', 'coordenada_interesse', 'endereco_interesse', 'tipo_interesse']] = None
            for ind in business.index:
                append_dataframe.at[ind, 'ponto_interesse'] = business.at[ind, 'name']
                append_dataframe.at[ind, 'coordenada_interesse'] = business.at[ind, 'geometry']['location']
                append_dataframe.at[ind, 'endereco_interesse'] = business.at[ind, 'vicinity']
                append_dataframe.at[ind, 'tipo_interesse'] = business.at[ind, 'types']
            interest_dataframe = interest_dataframe.append(append_dataframe, ignore_index=True)
            
            found_list.append(response.get('results'))
            print(f'\n\t- Quantity of found interest points: {len(found_list)}')
    
    interest_columns = interest_dataframe.columns
    original_columns = input_dataframe.columns
    interest_dataframe[original_columns] = input_dataframe.loc[row]
    interest_dataframe.columns = [original_columns+interest_columns]
    print(f'\n\t- Processed and organized DataFrame for {empreendimento}:\n{interest_dataframe}\n')
    interest_dataframe.to_csv(f'{path_output}businessCase?{empreendimento}?{cep}?.csv', sep=';')
