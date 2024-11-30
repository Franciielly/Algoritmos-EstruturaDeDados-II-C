"""
3. Jump Search
   - Compare o tempo de execução do Jump Search com o Binary Search em listas de diferentes tamanhos.
"""

import time
import random
from jumpSearch import*
from binarySearch import*

def comparar_algoritmos(lista):
    valor = random.choice(lista)  

    start_time = time.time()
    jump_search(lista, valor)
    jump_duration = time.time() - start_time

    start_time = time.time()
    binary_search(lista, valor)
    binary_duration = time.time() - start_time

    return jump_duration, binary_duration

tamanhos = [10, 100, 1000, 10000, 100000]
resultados = []

for tamanho in tamanhos:
    lista = sorted([random.randint(1, 1000000) for _ in range(tamanho)])
    jump_time, binary_time = comparar_algoritmos(lista)
    resultados.append((tamanho, jump_time, binary_time))

print("Tamanho da Lista   | Tempo Jump Search (s)     | Tempo Binary Search (s)")
for resultado in resultados:
    print(f"{resultado[0]:<18} | {resultado[1]:<25} | {resultado[2]:<10.6}")