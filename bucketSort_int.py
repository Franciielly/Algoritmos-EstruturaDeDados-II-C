"""
8. Bucket Sort
- Adapte o Bucket Sort para ordenar números inteiros positivos em intervalos maiores.
"""
def bucket_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    num_baldes = len(lista)
    baldes = [[] for _ in range(num_baldes)]

    for num in lista:
        indice = (num * num_baldes) // (max_val + 1)
        baldes[indice].append(num)
    
    for i in range(num_baldes):
        baldes[i].sort()
 
    lista_ordenada = []
    for balde in baldes:
        lista_ordenada.extend(balde)
    
    return lista_ordenada

if __name__ == "__main__":
    lista = []
    while True:
        numero = input("Digite um número(ou 'Enter'para encerrar): ")
        if numero.isdigit():
            lista.append(int(numero))
        elif numero == "":
            break
        else: 
            print("Por favor, digite número válido ou 'enter' para encerrar")

    lista_ordenada = bucket_sort(lista)
    print("Lista ordenada:", lista_ordenada)
