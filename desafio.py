"""
20. Desafios de Implementação
    - Crie um programa que permita ao usuário escolher um algoritmo de busca e ordenação para ordenar uma lista ou procurar um elemento, oferecendo comparações automáticas entre os métodos.
"""

import time
from binarySearch import binary_search
from jumpSearch import jump_search

def shell_sort(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2
    return lista

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
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def bucket_sort(lista):
    max_val = max(lista)
    tamanho = max_val / len(lista)
    baldes = [[] for _ in range(len(lista))]
    
    for num in lista:
        i = int(num // tamanho)
        if i != len(lista):
            baldes[i].append(num)
        else:
            baldes[len(lista) - 1].append(num)
    
    for i in range(len(lista)):
        baldes[i] = sorted(baldes[i])
    
    lista.clear()
    for balde in baldes:
        lista.extend(balde)
    return lista

def radix_sort(lista):
    def counting_sort(lista, exp):
        n = len(lista)
        saída = [0] * n
        contagem = [0] * 10
        
        for i in range(n):
            índice = lista[i] // exp
            contagem[índice % 10] += 1
        
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]
        
        i = n - 1
        while i >= 0:
            índice = lista[i] // exp
            saída[contagem[índice % 10] - 1] = lista[i]
            contagem[índice % 10] -= 1
            i -= 1
        
        for i in range(n):
            lista[i] = saída[i]
    
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort(lista, exp)
        exp *= 10
    return lista

#Algoritmo de busca
def interpolation_search(lista, alvo):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto and alvo >= lista[baixo] and alvo <= lista[alto]:
        if baixo == alto:
            if lista[baixo] == alvo:
                return baixo
            return -1
        pos = baixo + ((alto - baixo) // (lista[alto] - lista[baixo])) * (alvo - lista[baixo])
        if lista[pos] == alvo:
            return pos
        elif lista[pos] < alvo:
            baixo = pos + 1
        else:
            alto = pos - 1
    return -1

def exponential_search(lista, alvo):
    if lista[0] == alvo:
        return 0
    i = 1
    while i < len(lista) and lista[i] <= alvo:
        i *= 2
    return binary_search(lista[min(i//2, len(lista)): min(i, len(lista))], alvo)

def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return fim - inicio, resultado

def main():
    lista = []  # Lista onde os números serão armazenados
    tempos_ordem = {}
    tempos_busca = {}
    nomes_ordem = {}
    nomes_busca = {}

    while True:
        if not lista:
            while True:
                numeros = input("Digite um número(ou 'Enter' para encerrar): ")
                if numeros.isdigit():
                    lista.append(int(numeros))
                elif numeros == "":
                    break
                else:
                    print("Por favor, digite número válido ou 'enter' para encerrar")
        
        print("Escolha um algoritmo de ordenação:")
        print("1. Shell Sort")
        print("2. Merge Sort")
        print("3. Selection Sort")
        print("4. Bucket Sort")
        print("5. Radix Sort")
        escolha_ordem = int(input("Digite o número do algoritmo de ordenação: "))

        if escolha_ordem == 1:
            tempo, lista_ordenada = medir_tempo(shell_sort, lista)
            nome_algoritmo_ordem = "Shell Sort"
        elif escolha_ordem == 2:
            tempo, lista_ordenada = medir_tempo(merge_sort, lista)
            nome_algoritmo_ordem = "Merge Sort"
        elif escolha_ordem == 3:
            tempo, lista_ordenada = medir_tempo(selection_sort, lista)
            nome_algoritmo_ordem = "Selection Sort"
        elif escolha_ordem == 4:
            tempo, lista_ordenada = medir_tempo(bucket_sort, lista)
            nome_algoritmo_ordem = "Bucket Sort"
        elif escolha_ordem == 5:
            tempo, lista_ordenada = medir_tempo(radix_sort, lista)
            nome_algoritmo_ordem = "Radix Sort"
        else:
            print("Escolha inválida!")
            continue
        
        print(f"Lista ordenada: {lista_ordenada}")
        print(f"Tempo de execução para ordenação: {tempo:.6f} segundos")
        tempos_ordem[tempo] = lista_ordenada
        nomes_ordem[tempo] = nome_algoritmo_ordem

        print("\nEscolha um algoritmo de busca:")
        print("1. Busca Binária")
        print("2. Busca por Interpolação")
        print("3. Jump Search")
        print("4. Exponential Search")
        escolha_busca = int(input("Digite o número do algoritmo de busca: "))
        
        alvo = int(input("Digite o número a ser buscado: "))
        
        if escolha_busca == 1:
            tempo, resultado = medir_tempo(binary_search, lista_ordenada, alvo)
            nome_algoritmo_busca = "Busca Binária"
        elif escolha_busca == 2:
            tempo, resultado = medir_tempo(interpolation_search, lista_ordenada, alvo)
            nome_algoritmo_busca = "Busca por Interpolação"
        elif escolha_busca == 3:
            tempo, resultado = medir_tempo(jump_search, lista_ordenada, alvo)
            nome_algoritmo_busca = "Jump Search"
        elif escolha_busca == 4:
            tempo, resultado = medir_tempo(exponential_search, lista_ordenada, alvo)
            nome_algoritmo_busca = "Exponential Search"
        else:
            print("Escolha inválida!")
            continue
        
        if resultado != -1:
            print(f"Elemento encontrado no índice: {resultado}")
        else:
            print("Elemento não encontrado.")
        
        tempos_busca[tempo] = resultado
        nomes_busca[tempo] = nome_algoritmo_busca
        print(f"Tempo de execução para busca: {tempo:.6f} segundos")

        comparar = input("Deseja comparar os tempos anteriores? (S/N): ")
        if comparar.lower() == 's':
            print("\nTempos de ordenação anteriores:")
            for t, lista in tempos_ordem.items():
                print(f"Algoritmo: {nomes_ordem[t]} - Tempo: {t:.6f} segundos - Lista: {lista}")
            
            print("\nTempos de busca anteriores:")
            for t, resultado in tempos_busca.items():
                print(f"Algoritmo: {nomes_busca[t]} - Tempo: {t:.6f} segundos - Resultado: {resultado}")
        
        nova_lista = input("\nDeseja usar a mesma lista novamente? (S/N): ")
        if nova_lista.lower() != 's':
            lista = []

if __name__ == "__main__":
    main()
