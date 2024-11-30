"""
15. Busca e Ordenação em Strings
    - Adapte os algoritmos de ordenação (Merge Sort e Quick Sort) para ordenar palavras em ordem alfabética.
"""

from mergeSort import merge_sort

def quick_sort_palavras(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]
    menores = [palavra for palavra in lista[:-1] if palavra <= pivo]  
    maiores = [palavra for palavra in lista[:-1] if palavra > pivo] 

    return quick_sort_palavras(menores) + [pivo] + quick_sort_palavras(maiores)

palavras = []

while True: 
    palavra = input("Digite uma palavra (ou'Enter' para encerrar): ")
    if palavra.isalpha():
        palavras.append(palavra)
    elif palavra == "":
        break
    else:
        print("Por favor, digite apenas letras ou 'Enter' para encerrar.")

merge_sort(palavras)
print("\nOrdenado com Merge Sort:", palavras)

ordenado_quick = quick_sort_palavras(palavras)
print("Ordenado com Quick Sort:", ordenado_quick)


"""Utilize Binary Search para verificar se uma palavra específica está presente em uma lista de palavras ordenadas."""

from binarySearch import binary_search

while True: 
    palavra_procurada = input("\nDigite uma palavra para buscar: ")
    if palavra_procurada.isalpha():
        break
    else: 
        print("Por favor, digite apenas letras.")

resultado = binary_search(palavras, palavra_procurada)

if resultado != -1:
    print(f"A palavra '{palavra_procurada}' está no índice: {resultado}")
else:
    print(f"A palavra '{palavra_procurada}' não está na lista")