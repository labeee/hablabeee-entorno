import pandas as pd
from rich import print
from rich.progress import track
from rich.traceback import install
import time
install()

a = {'a': [1,2], 'b': [3,4]}
b = {'a': [5,6], 'b': [7,8]}
c = {'a': [9,10], 'b': [11,12]}
d = {'a': [13,14], 'b': [15,16]}

lista = [a, b, c, d]
print(lista)

df = pd.DataFrame(lista.pop(0))
print('-'*10)
for i in track(lista, description='[green]Concatenando[/green][blue] DataFrames[/blue]...'):
    time.sleep(2)
    new_df = pd.DataFrame(i)
    df = pd.concat([df, new_df], ignore_index=True, axis=0)
    print(df)
    print('-'*10)
