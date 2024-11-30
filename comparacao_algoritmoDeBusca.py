"""
12. Comparação de Algoritmos de Busca
 - Construa uma tabela comparativa dos tempos de execução de Binary Search, Interpolation Search, Jump Search e Exponential Search em listas de tamanhos diferentes.
"""
import random
import time
import pandas as pd
from binarySearch import binary_search
from jumpSearch import jump_search
from exponentialSearch import exponential_search

def interpolation_search(lista, elemento): 
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim and lista[inicio] <= elemento <= lista[fim]:
        if lista[inicio] == lista[fim]:
            if lista[inicio] == elemento:
                return inicio
            else:
                return -1
            
        meio = inicio + ((elemento - lista[inicio]) * (fim - inicio)) // (lista[fim] - lista[inicio])

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else: 
            inicio = meio - 1
    return -1

def comparar_algoritmos(lista, valor):

    start_time = time.time()
    binary_search(lista, valor)
    binary_duration = time.time() - start_time

    start_time = time.time()
    interpolation_search(lista, valor)
    interpolation_duration = time.time() - start_time

    start_time = time.time()
    jump_search(lista, valor)
    jump_duration = time.time() - start_time

    start_time = time.time()
    exponential_search(lista, valor)
    exponential_duration = time.time() - start_time

    return {
        "Binary Search": binary_duration,
        "Interpolation Search": interpolation_duration,
        "Jump Search": jump_duration,
        "Exponential Search": exponential_duration
    }

if __name__ == "__main__":
    tamanhos = [100, 1000, 10000, 100000]
    
    resultados = []

    for tamanho in tamanhos:
        lista = sorted([random.randint(0, 1000000) for _ in range(tamanho)])
        valor = random.choice(lista)
        
        tempos = comparar_algoritmos(lista, valor)
    
        resultados.append({
            "Tamanho da Lista": tamanho,
            "Binary Search": tempos['Binary Search'],
            "Interpolation Search": tempos['Interpolation Search'],
            "Jump Search": tempos['Jump Search'],
            "Exponential Search": tempos['Exponential Search']
        })

    df = pd.DataFrame(resultados)

    print(df)
