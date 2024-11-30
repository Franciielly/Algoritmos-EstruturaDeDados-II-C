"""
11. Ternary Search
- Compare seu desempenho com o Binary Search.
"""

import random
import time
from binarySearch import binary_search
from ternarySearch import ternary_search

def comparar_algoritmos(lista):
    valor = random.choice(lista)  

    start_time = time.time()
    ternary_search(lista, 0, len(lista) -1 , valor)
    ternary_duration = time.time() - start_time

    start_time = time.time()
    binary_search(lista, valor)
    binary_duration = time.time() - start_time

    return ternary_duration, binary_duration, valor
   
if __name__ == "__main__":
    lista = []
    while True: 
        numeros = input("Digite um número(ou 'Enter' para encerrar): ")
        if numeros.isdigit():
            lista.append(int(numeros))
        elif numeros == "":
            break
        else:
            print("Por favor, digite número válidos ou 'Enter' para encerrar.")

    lista.sort()

    ternary_duration, binary_duration, valor = comparar_algoritmos(lista)
    
    print(f"Valor buscado: {valor}")
    print(f"Tempo de execução do Ternary Search: {ternary_duration:.6f} segundos")
    print(f"Tempo de execução do Binary Search: {binary_duration:.6f} segundos")