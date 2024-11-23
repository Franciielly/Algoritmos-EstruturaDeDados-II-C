"""
2. Interpolation Search
    - Crie uma função que implemente o Interpolation Search e teste-a em listas ordenadas com intervalos uniformes e não uniformes. Compare com o Binary Search.
 """

from binary_search import binary_search

def interpolation_search(lista, elemento): 
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim and lista[inicio] <= elemento <= lista[fim]:
        if lista[inicio] == lista[fim]:
            if lista[inicio] == elemento:
                return inicio
            else:
                return -1
            
        meio = inicio + ((elemento - lista[inicio]) * (fim - inicio)) // (lista[fim] - lista[inicio])

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else: 
            inicio = meio - 1
    return -1

lista_nao_uniforme = []
print("Digite números com intervalos não uniforme(ou digite 'sair' para encerrar) ")
while True:
    numero = input("Número: ")
    if numero.lower() == "sair":
        break
    if numero.isdigit():
        lista_nao_uniforme.append(int(numero))
    else:
        print("Por favor, digite número válido ou 'sair' para encerrar")

lista_nao_uniforme.sort()
lista_uniforme = [i * 5 for i in range(1,50)] 

i = int(input("Digite quantos números deseja buscar: "))

lista_buscar =[]

for n in range(i):
    elemento = input("número: ")
    if elemento.isdigit():
        lista_buscar.append(int(elemento))
    else:
        print("Digite apenas número")

print("\nLista com intervalos uniformes\n")
for value in lista_buscar:
    resultado = interpolation_search(lista_uniforme, value)
    if resultado != -1:
        print(f"Interpolation - {value} encontrado no índice: {resultado}")
    else:
        print(f"Interpolation - {value} não encontrado")
    resultado = binary_search(lista_uniforme, value)
    if resultado != -1:
        print(f"binary - {value} encontrado no índice: {resultado}")
    else:
        print(f"binary - {value} não encontrado")

print("\nlista com intervalos não uniformes\n")
for value in lista_buscar:
    resultado = interpolation_search(lista_nao_uniforme, value)
    if resultado != -1:
        print(f"Interpolation - {value} encontrado no índice: {resultado}")
    else:
        print(f"Interpolation - {value} não encontrado")
    resultado = binary_search(lista_nao_uniforme, value)
    if resultado != -1:
        print(f"binary - {value} encontrado no índice: {resultado}")
    else:
        print(f"binary - {value} não encontrado")

"""
- Identifique casos em que o Interpolation Search é mais eficiente que o Binary Search.

O interpolation Search é mais eficiente que o binary search em listas grandes, ordenadas e com intervalos uniformemente distribuído, por exemplo, em uma lista telefônica organizada em ordem alfabética.
"""