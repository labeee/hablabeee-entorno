coordenadas = '-25.997858098017268/-52.22127528495758' # Atualmente são coordenadas de Covó, em Mangueirinha (PR)
coordinates = coordenadas.split('/')
key = 'INSIRA SUA CHAVE'

import googlemaps
import pandas as pd

client = googlemaps.Client(key)

response = client.places_nearby(
                location=(coordinates[0], coordinates[1]),
                keyword='Mercado',
                rank_by='distance'
            )

print(response)

with open('Teste_de_Retorno.txt', 'w') as pn:
    pn.write('\n\n'.join(str(response).split("business_status")))
    pn.close()

pontonemo = pd.DataFrame(response.get('results'))

print(pontonemo)

pontonemo.to_csv('DataFrame_de_Teste.csv', sep=';')
