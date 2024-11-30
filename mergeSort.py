"""
6. Merge Sort
   - Implemente o Merge Sort para ordenar uma lista de números inteiros.
"""

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

if __name__ == "__main__":
    lista = []

    while True: 
        numeros = input("Digite um número(ou 'Enter'para encerrar): ")
        if numeros.isdigit():
            lista.append(int(numeros))
        elif numeros == "":
            break
        else:
            print("Por favor, digite número válido ou 'enter' para encerrar")

    print("Lista original:", lista)
    merge_sort(lista)
    print("Lista ordenada:", lista)
