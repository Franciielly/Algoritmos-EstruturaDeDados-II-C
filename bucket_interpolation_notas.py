""" 
17. Busca e Ordenação em Dados Reais
    - Implemente Bucket Sort para ordenar as notas de uma turma de alunos, classificadas entre 0 e 100. Em seguida, utilize o Interpolation Search para encontrar um aluno com uma nota específica.
"""

def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    valor_minimo = min(arr, key=lambda x: x[1])[1]
    valor_maximo = max(arr, key=lambda x: x[1])[1]
    intervalo_balde = (valor_maximo - valor_minimo) / n
    baldes = [[] for _ in range(n)]
    
    for aluno, nota in arr:
        indice = int((nota - valor_minimo) / intervalo_balde)
        if indice == n:
            indice -= 1
        baldes[indice].append((aluno, nota))
    
    for i in range(n):
        baldes[i].sort(key=lambda x: x[1])
    
    arr_ordenado = []
    for balde in baldes:
        arr_ordenado.extend(balde)
    
    return arr_ordenado

def interpolation_search(arr, alvo):
    baixo = 0
    alto = len(arr) - 1
    
    while baixo <= alto and alvo >= arr[baixo][1] and alvo <= arr[alto][1]:
        posicao = baixo + ((alvo - arr[baixo][1]) * (alto - baixo)) // (arr[alto][1] - arr[baixo][1])
        
        if arr[posicao][1] == alvo:
            return posicao
        elif arr[posicao][1] < alvo:
            baixo = posicao + 1
        else:
            alto = posicao - 1
    
    return -1

alunos = [("Carlos", 85), ("Ana", 90), ("Lucas", 78), ("Maria", 88), ("Pedro", 92), 
          ("Júlia", 65), ("Rafael", 99), ("Fernanda", 73), ("Eduardo", 58), ("Beatriz", 100)]

alunos_ordenados = bucket_sort(alunos)
print("Alunos ordenados por nota:", alunos_ordenados)

nota_buscada = 92
indice = interpolation_search(alunos_ordenados, nota_buscada)

if indice != -1:
    aluno, nota = alunos_ordenados[indice]
    print(f"A nota {nota_buscada} foi encontrada com o aluno {aluno}.")
else:
    print(f"A nota {nota_buscada} não foi encontrada.")
