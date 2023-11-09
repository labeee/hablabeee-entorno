import googlemaps


# Coordenadas de origem: LabEEE
# Coordenadas destino: LayBack Park (Lagoa da Conceição), Ponte Hercílio Luz, Praia do Cacupé, Aeroporto Internacional de Florianópolis, Praia do Moçambique

pin_point = {'lat': '-27.599566988312336', 'lng': '-48.514684796437336'}
coord_destinations = [
    {'lat': '-27.60457411150869', 'lng': '-48.4659156690778'}, 
    {'lat': '-27.593616487551916', 'lng': '-48.56541470750463'}, 
    {'lat': '-27.53115583401214', 'lng': '-48.524572211500725'},
    {'lat': '-27.674247321077846', 'lng': '-48.54620990213489'},
    {'lat': '-27.52304917870192', 'lng': '-48.41672685158437'}
    ]


key = 'INSIRA SUA CHAVE'

client = googlemaps.Client(key)

response = client.distance_matrix(
                origins=pin_point,
                destinations=coord_destinations,
                mode='walking',
                language='pt-BR',
                units='metric'
                )

print(response)

with open(r'testingPlayground/Teste_de_Retorno_Matrix.txt', 'w') as lab:
    lab.write(str(response))
    lab.close()
