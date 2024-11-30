"""
16. Aplicação Prática de Busca
    - Use o Binary Search para procurar um livro específico por ISBN em uma lista ordenada de registros de biblioteca.
"""
def binary_search(lista, chave, chave_busca):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio][chave] == chave_busca:
            return lista[meio] 
        elif lista[meio][chave] < chave_busca:
            inicio = meio + 1 
        else:
            fim = meio - 1 
    
    return None  

biblioteca = [
    {"isbn": "0001", "titulo": "Introdução à Programação", "autor": "João Silva"},
    {"isbn": "0002", "titulo": "Estruturas de Dados", "autor": "Maria Souza"},
    {"isbn": "0003", "titulo": "Algoritmos Avançados", "autor": "Carlos Pereira"},
    {"isbn": "0004", "titulo": "Redes de Computadores", "autor": "Ana Costa"},
    {"isbn": "0005", "titulo": "Inteligência Artificial", "autor": "Paulo Lima"}
]

isbn_procurado = input("Digite o ISBN do livro procurado: ")

livro_encontrado = binary_search(biblioteca, "isbn", isbn_procurado)

if livro_encontrado:
    print("Livro encontrado!")
    print(f"ISBN: {livro_encontrado['isbn']}")
    print(f"Título: {livro_encontrado['titulo']}")
    print(f"Autor: {livro_encontrado['autor']}")
else:
    print("Livro não encontrado.")
