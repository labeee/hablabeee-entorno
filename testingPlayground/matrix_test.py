import pandas as pd
from glob import glob

ex = {
'destination_addresses': ['R. Henrique Vera do Nascimento, 320 - Lagoa da Conceição, Florianópolis - SC, 88062-020, Brasil', 'Pte. Hercílio Luz, 1400 - Centro, Florianópolis - SC, 88010-150, Brasil', 'Estrada Haroldo Soares Glavan, 1178 - Cacupé, Florianópolis - SC, 88050-005, Brasil', 'Boulevard 14/32 — Aeroporto de Florianópolis - Rod. Ac. ao Aeroporto - Base Aérea, Florianópolis - SC, 88047-902, Brasil', 'Estrada sem nome - São João do Rio Vermelho, Florianópolis - SC, Brasil'], 
'origin_addresses': ['R. João Pio Duarte Silva, 205 - Córrego Grande, Florianópolis - SC, 88037-000, Brasil'], 
'rows': [
{'elements': [
	{'distance': {'text': '7,1 km', 'value': 7079}, 'duration': {'text': '1 hora 44 minutos', 'value': 6257}, 'status': 'OK'}, 
	{'distance': {'text': '6,3 km', 'value': 6276}, 'duration': {'text': '1 hora 48 minutos', 'value': 6494}, 'status': 'OK'}, 
	{'distance': {'text': '13,8 km', 'value': 13794}, 'duration': {'text': '3 horas 11 minutos', 'value': 11445}, 'status': 'OK'}, 
	{'distance': {'text': '14,7 km', 'value': 14735}, 'duration': {'text': '3 horas 21 minutos', 'value': 12046}, 'status': 'OK'}, 
	{'distance': {'text': '21,2 km', 'value': 21186}, 'duration': {'text': '5 horas 1 minuto', 'value': 18043}, 'status': 'OK'}
	]}], 
'status': 'OK'
}

rows = ex.get('rows')[0].get('elements')
df_filtered = pd.DataFrame(rows)
df_filtered.drop(columns=['status'], axis=1, inplace=True)
print(df_filtered)
df_filtered.to_csv(f'testingPlayground/example_matrix.csv', sep=';')

for i in df_filtered.index:
    df_filtered.at[i, 'distance'] = df_filtered.at[i, 'distance'].get('value')
    df_filtered.at[i, 'duration'] = df_filtered.at[i, 'duration'].get('value')
df_filtered.columns = ['distance (meters)', 'duration (seconds)']
print(df_filtered)
df_filtered.to_csv(f'testingPlayground/example_filtered_matrix.csv', sep=';')
