"""
4. Exponential Search
   - Implemente o algoritmo Exponential Search para localizar um elemento em uma lista ordenada.
"""

def binary_search(lista, inicio, fim, valor):
    while inicio <= fim:
        meio = inicio + (fim - inicio) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else: 
            fim = meio - 1
    return -1
        
def exponential_search(lista, valor):
    if lista[0] == valor:
        return 0

    i = 1
    while i < len(lista) and lista[i] <= valor:
        i = i * 2
    
    return binary_search (lista, i // 2, min(i, len(lista) - 1), valor)

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
        
    lista.sort()

    valor = int(input("Digite o número que deseja buscar: "))
    
    resultado = exponential_search(lista, valor)

    if resultado != -1:
        print(f"{valor} encontrado no índice: {resultado}")
    else:
        print(f"{valor} não encontrado na lista")
    