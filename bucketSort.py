"""
8. Bucket Sort
   - Implemente o Bucket Sort para ordenar uma lista de números em ponto flutuante no intervalo (0, 1).
"""
def bucket_sort(lista):
    n = len(lista)
    if n <= 1:
        return lista
    
    baldes = [[] for _ in range(n)]
    
    for num in lista:
        indice = int(num * n)  
        baldes[indice].append(num)
    
    for i in range(n):
        baldes[i] = sorted(baldes[i])
    
    lista_ordenada = []
    for balde in baldes:
        lista_ordenada.extend(balde)
    
    return lista_ordenada

lista = [0.42, 0.32, 0.23, 0.56, 0.71, 0.12, 0.75]
lista_ordenada = bucket_sort(lista)
print("Lista ordenada:", lista_ordenada)
