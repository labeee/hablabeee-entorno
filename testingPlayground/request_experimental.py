import pandas as pd
import googlemaps
# Atualmente são coordenadas de Covó, em Mangueirinha (PR)
coordenadas = '-25.997858098017268/-52.22127528495758'

coordinates = coordenadas.split('/')
key = 'INSIRA SUA CHAVE'


client = googlemaps.Client(key)

response = client.places_nearby(
    location=(coordinates[0], coordinates[1]),
    keyword='Mercado',
    rank_by='distance'
)

print(response)

with open(r'testingPlayground/Teste_de_Retorno.txt', 'w') as pn:
    pn.write('\n\n'.join(str(response).split("business_status")))
    pn.close()

dataframe = pd.DataFrame(response.get('results'))

print(dataframe)

dataframe.to_csv(r'testingPlayground/DataFrame_de_Teste.csv', sep=';')
