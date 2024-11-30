"""
10. Quick Sort
- Analise o desempenho do Quick Sort em listas quase ordenadas e completamente desordenadas.
"""
import random
import time
import sys

sys.setrecursionlimit(2000)

def particionar(lista, baixo, alto, criterio):
    if criterio == 'primeiro':
        pivo = lista[baixo]
        lista[baixo], lista[alto] = lista[alto], lista[baixo]  
    elif criterio == 'ultimo':
        pivo = lista[alto]
    elif criterio == 'meio':
        meio = (baixo + alto) // 2
        lista[meio], lista[alto] = lista[alto], lista[meio]  
        pivo = lista[alto]
    elif criterio == 'aleatorio':
        indice_pivo = random.randint(baixo, alto)
        lista[indice_pivo], lista[alto] = lista[alto], lista[indice_pivo]
        pivo = lista[alto]
    
    i = baixo - 1
    for j in range(baixo, alto):
        if lista[j] < pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

def quick_sort(lista, baixo, alto, criterio, profundidade_max=1000):
    if baixo < alto:
        if profundidade_max == 0:
            return
        pivo_index = particionar(lista, baixo, alto, criterio)
        quick_sort(lista, baixo, pivo_index - 1, criterio, profundidade_max - 1)
        quick_sort(lista, pivo_index + 1, alto, criterio, profundidade_max - 1)

def gerar_lista_quase_ordenada(tamanho):
    lista = list(range(tamanho))
    random.shuffle(lista[int(tamanho / 2):])  
    return lista

def gerar_lista_desordenada(tamanho):
    return [random.randint(0, 10000) for _ in range(tamanho)]

tamanhos = [100, 1000]

criterios = ['meio', 'aleatorio']

for tamanho in tamanhos:
    print(f"Teste com lista de tamanho {tamanho}:")

    lista_quase_ordenada = gerar_lista_quase_ordenada(tamanho)
    lista_desordenada = gerar_lista_desordenada(tamanho)

    for criterio in criterios:
        print(f"  Teste com pivô '{criterio}':")
        
        inicio = time.time()
        quick_sort(lista_quase_ordenada, 0, len(lista_quase_ordenada) - 1, criterio)
        tempo_quase_ordenada = time.time() - inicio
        
        inicio = time.time()
        quick_sort(lista_desordenada, 0, len(lista_desordenada) - 1, criterio)
        tempo_desordenada = time.time() - inicio
        
        print(f"    Tempo para lista quase ordenada (pivô '{criterio}'): {tempo_quase_ordenada:.5f} segundos")
        print(f"    Tempo para lista completamente desordenada (pivô '{criterio}'): {tempo_desordenada:.5f} segundos\n")
    
resposta = """
- Listas quase ordenadas: O Quick Sort pode se comportar mal com pivôs fixos (ex.: primeiro ou último), levando a uma complexidade de O(n²). Com uma boa escolha de pivô, o desempenho melhora consideravelmente. 
- Listas completamente desordenadas: O Quick Sort geralmente tem bom desempenho (O(n log n)) se o pivô for escolhido de maneira eficiente, como pivô aleatório ou pivô do meio.
 """
print(resposta)