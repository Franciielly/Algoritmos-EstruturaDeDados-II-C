"""10. Quick Sort
    - Implemente o Quick Sort utilizando diferentes critérios para escolha do pivô (ex.: primeiro elemento, último elemento, elemento do meio).
"""
def particionar(lista, baixo, alto, criterio):
    if criterio == "primeiro":
        lista[baixo], lista[alto] = lista[alto], lista[baixo]
    elif criterio == "ultimo":
        lista[alto], lista[alto] = lista[alto], lista[alto]
    elif criterio == "meio":
        meio = (baixo + alto) // 2
        lista[meio], lista[alto] = lista[alto], lista[meio]
    
    pivo = lista[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if lista[j] < pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

def quick_sort(lista, baixo, alto, criterio="ultimo"):
    if baixo < alto:
        pivo_index = particionar(lista, baixo, alto, criterio)
        quick_sort(lista, baixo, pivo_index - 1, criterio)
        quick_sort(lista, pivo_index + 1, alto, criterio)

listas_de_testes = [
    [42, 56, 23, 85, 12],
    [87632, 35478, 90876, 23123, 56892],
    [385759283, 128375102, 984758394, 193847519, 231908573]
]

criterios = ["primeiro", "ultimo", "meio"]

for criterio in criterios:
    for lista in listas_de_testes:
        lista_original = lista.copy()
        quick_sort(lista, 0, len(lista) - 1, criterio)
        print(f"Critério: {criterio} | Original: {lista_original} -> Ordenado: {lista}")
    print("\n")