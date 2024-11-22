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
            inicio= meio - 1

    return -1


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




"""
- Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.

A lista deve estar ordenada porque o algoritmo utiliza o método "Dividir para Conquistar". Após verificar o elemento do meio da lista, ele descarta uma das metades com base na comparação. Em uma lista desordenada, se o meio não for o elemento buscado, é possível que o elemento esteja na metade descartada.

Exemplo: Lista Ordenada
Lista: [2, 4, 6, 7, 14, 24]
Elemento buscado: 7

- O algoritmo verifica o meio da lista, que é 6.
- Como 7 > 5, o algoritmo descarta a metade esquerda.
- Nova lista considerada é: [7, 14, 24].
- O novo meio é 14.
- Como 7 < 9, descartamos a metade direita e a nova sublista é [7].
- A lista tem apenas um elemento, 7, que é o nosso número procurado.


Exemplo: Lista Desordenada
Lista: [10, 2, 6, 8, 4]
Elemento buscado: 10

- O algoritmo verifica o elemento do meio da lista, que é 6.
- Como 10 > 6, o algoritmo descarta a metade esquerda.
- Como a lista está desordenada, o número 10 foi descartado.
"""
