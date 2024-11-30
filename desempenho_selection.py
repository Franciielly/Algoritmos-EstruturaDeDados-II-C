"""
7. Selection Sort
- Analise o desempenho do Selection Sort em listas pequenas, médias e grandes.
"""
import random
import time

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j

def measure_time(n):
    arr = random.sample(range(n*10), n)  
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    return end_time - start_time

sizes = [100, 1000, 10000]  
for size in sizes:
    time_taken = measure_time(size)
    print(f"Tempo para ordenar uma lista de tamanho {size}: {time_taken:.5f} segundos")

resposta = """
Pequenas listas: O Selection Sort pode ser aceitável, pois o número de comparações não é muito grande, e o impacto da complexidade O(n²) é pequeno.

Listas médias: O algoritmo começa a mostrar limitações, pois o número de comparações cresce rapidamente, tornando o tempo de execução perceptível.

Listas grandes: O desempenho se deteriora consideravelmente, com o tempo de execução se tornando impraticável devido ao crescimento quadrático das comparações (O(n²)).
"""

print(resposta)
