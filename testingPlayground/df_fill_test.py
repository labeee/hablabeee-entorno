import pandas as  pd
import warnings
warnings.filterwarnings('ignore')

df_1 = {
    "Cidade": 
        [
            'Maceio', 
            'Curitiba', 
            'Flor do Sertao'
        ], 
    "Data": 
        [
            '01', 
            '02', 
            '03'
        ]}
df_1 = pd.DataFrame(df_1)
print('\n'*5)
print(df_1)


df_2 = {
    "Pessoa":
    [
        'Francisco',
        'Angela',
        'Marcelo'
    ]
}
df_2 = pd.DataFrame(df_2)
print('\n'*5)
print(df_2)
print('\n'*5)


colunas_cidade = df_1.columns
print(colunas_cidade)
print('\n'*5)
colunas_pessoas = df_2.columns
print(colunas_pessoas)
print('\n'*5)
df_2[colunas_cidade] = df_1.loc[0]
print(df_2)
print('\n'*5)
df_2.columns = [colunas_cidade.tolist()+colunas_pessoas.tolist()]
print(df_2)
print('\n'*5)
