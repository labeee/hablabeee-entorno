import pandas as pd

sla = {'a': [1,2], 'b': [3,4]}
df = pd.DataFrame(sla)

df.to_csv('testingPlayground/teste .csv')

# Não aceita:
# * \ ? > < . 

# Aceita
# + - _ # $ % & @ ! ~ ^ , ESPAÇO