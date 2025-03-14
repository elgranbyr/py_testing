def normalizar_lista(lista):
    return list(set(lista))  # Elimina duplicados

numeros = [1, 2, 2, 3, 3, 3, 4,5,6,5,6,10,11,10,11,12,12,13,13,14,14,15,15]
print(normalizar_lista(numeros))                           # fx(x)
print(normalizar_lista(normalizar_lista(numeros))) # f(g(x))
