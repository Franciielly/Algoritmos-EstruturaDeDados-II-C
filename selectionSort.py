""" 
7. Selection Sort
   - Desenvolva o Selection Sort e acompanhe cada iteração mostrando como a lista é organizada passo a passo.
"""

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print(f"Iteração {i + 1}: {lista}")

if __name__ == "__main__":
    lista = [13, 12, 28, 25, 19, 16, 7, 22, 6, 8]
    print("Lista original:", lista)
    selection_sort(lista)
    print("Lista ordenada:", lista)