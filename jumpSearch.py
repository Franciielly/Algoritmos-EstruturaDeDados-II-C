"""
3. Jump Search
   - Desenvolva o algoritmo Jump Search e determine o tamanho ideal do "salto" para uma lista de tamanho N.
"""

def jump_search(lista, valor):
    tamanho = len(lista)
    salto = int(tamanho * 0.5)

    inicio = 0
    fim = min(salto, tamanho)

    while fim < tamanho and lista [min(fim, tamanho) - 1] < valor:
        inicio = fim
        fim += salto
        if inicio >= tamanho:
            return -1

    for i in range(inicio, min(fim,tamanho)):
        if lista[i] == valor:
            return i

    return -1 

if __name__ == "__main__":
    lista = []
    while True:
        numero = input("Digite um número(ou 'enter' para encerrar): ")
        if numero.isdigit():
            lista.append(int(numero))
        elif numero == "":
            break
        else:
            print("Por favor, digite número válido ou 'enter' para encerrar")
    
    lista.sort()
    
    valor = int(input("Digite o número que deseja buscar: "))
    
    resultado = jump_search(lista, valor)

    if resultado != -1:
        print(f"{valor} encontrado no índice: {resultado}")
    else: 
        print(f"{valor} não encontrado na lista")