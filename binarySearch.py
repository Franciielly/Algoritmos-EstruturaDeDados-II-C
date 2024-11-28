"""
1. Binary Search
   - Implemente o algoritmo Binary Search em uma lista ordenada e encontre o índice de um elemento dado.
"""

def binary_search(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim ) // 2

        if lista[meio] == elemento:
            return meio

        elif lista[meio] < elemento:
            inicio = meio + 1
        
        else:
            fim = meio - 1

    return -1


if __name__ == "__main__":
    lista = []
    print("Digite o número da lista um por vez(ou digite 'sair' para encerrar) ")
    while True:
        entrada = input("Número: ").strip()
        if entrada.lower() == "sair":
            break
        if entrada.isdigit():
            lista.append(int(entrada))
        else:
            print("Por favor, digite número válido ou 'sair' para encerrar")

    lista.sort()

    numero_buscado = int(input("Digite o número que deseja buscar: "))

    resultado = binary_search(lista, numero_buscado)

    if resultado != -1:
        print(f"{numero_buscado} encontrado no índice: {resultado}")
    else:
        print(f"{numero_buscado} não encontrado na lista")