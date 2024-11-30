"""
5. Shell Sort
   - Implemente o Shell Sort com diferentes sequências de intervalo (ex.: Shell, Knuth, Hibbard). Compare os tempos de execução.
"""

import time
import random

def shell_sort(arr, sequencia):
    n = len(arr)
    for intervalo in sequencia:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i
            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo
            arr[j] = temp

def sequencia_shell(n):
    intervalo = n // 2
    sequencia = []
    while intervalo > 0:
        sequencia.append(intervalo)
        intervalo //= 2
    return sequencia

def sequencia_knuth(n):
    sequencia = []
    intervalo = 1
    while intervalo < n:
        sequencia.insert(0, intervalo)
        intervalo = 3 * intervalo + 1
    return sequencia

def sequencia_hibbard(n):
    sequencia = []
    k = 1
    while (1 << k) - 1 < n:
        sequencia.insert(0, (1 << k) - 1)
        k += 1
    return sequencia

def medir_tempo(lista, func_sequencia):
    copia_lista = lista.copy()
    sequencia = func_sequencia(len(lista))
    inicio_tempo = time.time()
    shell_sort(copia_lista, sequencia)
    fim_tempo = time.time()
    return fim_tempo - inicio_tempo

tamanho = 10000

dados = [random.randint(1, 100000) for _ in range(tamanho)]

tempo_shell = medir_tempo(dados, sequencia_shell)
tempo_knuth = medir_tempo(dados, sequencia_knuth)
tempo_hibbard = medir_tempo(dados, sequencia_hibbard)

print("Resultados de tempo de execução para diferentes sequências de intervalo:")
print(f"Sequência Shell: {tempo_shell:.6f} segundos")
print(f"Sequência Knuth: {tempo_knuth:.6f} segundos")
print(f"Sequência Hibbard: {tempo_hibbard:.6f} segundos")
