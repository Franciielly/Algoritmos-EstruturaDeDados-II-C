"""
13. Comparação de Algoritmos de Ordenação
    - Ordene a mesma lista utilizando Shell Sort, Merge Sort, Selection Sort, Quick Sort, Bucket Sort e Radix Sort. Registre os tempos de execução e número de comparações realizadas.
"""

import time
import random

def medir_algoritmo(algoritmo):
    def executar(*args, **kwargs):
        comparacoes = [0]
        inicio = time.time()
        resultado = algoritmo(*args, comparacoes=comparacoes, **kwargs)
        fim = time.time()
        tempo = fim - inicio
        return resultado, tempo, comparacoes[0]
    return executar

tam_lista = 1000
lista = [random.randint(0, 1000) for _ in range(tam_lista)]

@medir_algoritmo
def shell_sort(arr, comparacoes):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparacoes[0] += 1
                arr[j] = arr[j - gap]
                j -= gap
            comparacoes[0] += 1 if j >= gap else 0
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort_interno(arr, comparacoes):
    def merge(esq, dir):
        ordenado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            comparacoes[0] += 1
            if esq[i] < dir[j]:
                ordenado.append(esq[i])
                i += 1
            else:
                ordenado.append(dir[j])
                j += 1
        ordenado.extend(esq[i:])
        ordenado.extend(dir[j:])
        return ordenado

    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esq = merge_sort_interno(arr[:meio], comparacoes)
    dir = merge_sort_interno(arr[meio:], comparacoes)
    return merge(esq, dir)

@medir_algoritmo
def merge_sort(arr, comparacoes):
    return merge_sort_interno(arr, comparacoes)

@medir_algoritmo
def quick_sort(arr, comparacoes):
    def particionar(ini, fim):
        pivo = arr[fim]
        i = ini - 1
        for j in range(ini, fim):
            comparacoes[0] += 1
            if arr[j] < pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
        return i + 1

    def quick_sort_interno(ini, fim):
        if ini < fim:
            pi = particionar(ini, fim)
            quick_sort_interno(ini, pi - 1)
            quick_sort_interno(pi + 1, fim)

    quick_sort_interno(0, len(arr) - 1)
    return arr

@medir_algoritmo
def bucket_sort(arr, comparacoes):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    size = max_val // len(arr) + 1
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        comparacoes[0] += 1
        buckets[arr[i] // size].append(arr[i])
    for bucket in buckets:
        bucket.sort()
    return [item for bucket in buckets for item in bucket]

@medir_algoritmo
def radix_sort(arr, comparacoes):
    max_val = max(arr) if arr else 0
    exp = 1
    while max_val // exp > 0:
        output = [0] * len(arr)
        count = [0] * 10
        for i in arr:
            index = i // exp % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        for i in range(len(arr)):
            comparacoes[0] += 1
            arr[i] = output[i]
        exp *= 10
    return arr

def executar_comparacao():
    algoritmos = [
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Bucket Sort", bucket_sort),
        ("Radix Sort", radix_sort),
    ]

    for nome, algoritmo in algoritmos:
        arr = lista[:]
        _, tempo, comparacoes = algoritmo(arr)
        print(f"{nome}: {tempo:.6f}s, {comparacoes} comparacoes")

executar_comparacao()
