"""
11. Ternary Search
    - Desenvolva o algoritmo Ternary Search para localizar um elemento em uma lista ordenada.
"""
def ternary_search(lista, esquerda, direita, valor):
    if direita >= esquerda:
        meio1 = esquerda + (direita - esquerda) // 3
        meio2 = direita - (direita - esquerda) // 3
        
        if lista[meio1] == valor:
            return meio1
        if lista[meio2] == valor:
            return meio2
        
        if valor < lista[meio1]:
            return ternary_search(lista, esquerda, meio1 - 1, valor)
        elif valor > lista[meio2]:
            return ternary_search(lista, meio2 + 1, direita, valor)
        else:
            return ternary_search(lista, meio1 + 1, meio2 - 1, valor)
    
    return -1

if __name__ == "__main__":
    lista = []
    while True: 
        numeros = input("Digite um número(ou 'Enter' para encerrar): ")
        if numeros.isdigit():
            lista.append(int(numeros))
        elif numeros == "":
            break
        else:
            print("Por favor, digite número válidos ou 'Enter' para encerrar.")

    lista.sort()

    valor = int(input("Digite o número que deseja buscar: "))

    resultado = ternary_search(lista, 0, len(lista) -1 , valor)

    if resultado != -1:
        print(f"{valor} encontrado no índice: {resultado}")
    else:
        print(f"{valor} não encontrado na lista.")