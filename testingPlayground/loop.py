
lista = [0,1,2,3,4,5,6,7,8,9,10]
results = 4
search = 5
lista_appendada = []

print(f'\nEsperado: {lista}\nResultados: {results}\nDesejados: {search}\n')

for ind in lista:
    if (ind < search) and (ind < results):
        print(ind)
        lista_appendada.append(ind)

print(f'\nResultado: {lista_appendada} de len {len(lista_appendada)}\n')