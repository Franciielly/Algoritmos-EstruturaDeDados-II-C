"""
6. Merge Sort
- Modifique o Merge Sort para ordenar strings em ordem alfabética.
"""

from mergeSort import*

palavras = []
while True: 
    palavra = input("Digite uma palavra (ou 'Enter'para encerrar): ")
    if palavra.isalpha():
        palavras.append(palavra)
    elif palavra == "":
        break
    else:
        print("Por favor, digite letras ou 'enter' para encerrar")

print("Lista original:", palavras)
merge_sort(palavras)
print("Lista ordenada:", palavras)