"""
9. Radix Sort
   - Implemente o Radix Sort para ordenar uma lista de números inteiros. Teste-o com números de diferentes tamanhos (ex.: 2 dígitos, 5 dígitos, 10 dígitos).
"""
def contagem_ordenacao(lista, exp):
    n = len(lista)
    resultado = [0] * n
    contagem = [0] * 10 
   
    for i in range(n):
        indice = lista[i] // exp
        contagem[indice % 10] += 1
    
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    i = n - 1

    while i >= 0:
        indice = lista[i] // exp
        resultado[contagem[indice % 10] - 1] = lista[i]
        contagem[indice % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = resultado[i]

def radix_sort(lista):
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        contagem_ordenacao(lista, exp)
        exp *= 10

listas_de_testes = [
    [42, 56, 23, 85, 12],  
    [87632, 35478, 90876, 23123, 56892],  
    [385759283, 128375102, 984758394, 193847519, 231908573] 
]

for lista in listas_de_testes:
    lista_original = lista.copy()
    radix_sort(lista)
    print(f"Original: {lista_original} - Ordenado: {lista}")

