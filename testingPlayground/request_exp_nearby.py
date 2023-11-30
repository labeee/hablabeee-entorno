import googlemaps

# Atualmente são coordenadas do LabEEE
coordenadas = '-27.599669553295215/-48.5147299581353'
coordinates = coordenadas.split('/')

key = 'INSIRA SUA CHAVE'

client = googlemaps.Client(key)

response = client.places_nearby(
    location=(coordinates[0], coordinates[1]),
    keyword='Posto de saude',
    rank_by='distance'
)

print(response)

with open(r'testingPlayground/Teste_de_Retorno_Nearby.txt', 'w') as covo:
    covo.write('\n\n'.join(str(response).split("business_status")))
    covo.close()
