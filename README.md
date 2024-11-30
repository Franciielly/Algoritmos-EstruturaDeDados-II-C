# **Questões:**
# **1.	Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.**
A lista precisa estar ordenada, pois o Binary Search elimina um lado. Se o número desejado for maior que o do meio, ele elimina toda a parte esquerda. Dito isso, em uma lista desordenada, pode ser que o número desejado esteja no lado que será eliminado.

### Ex: [1,2,3,4,5] – lista ordenada
     Número desejado = 4      
     Meio = 3 
     elimina toda esquerda (menores que meio)
     meio = 4
     Elemento encontrado!
     
Ex  : [4,1,2,3,4] – lista desordenada
     Número desejado = 4
     Meio = 2
     elimina toda esquerda
     4 foi eliminado.
  
# **2.	 Identifique casos em que o Interpolation Search é mais eficiente que o Binary Search.**
  O Interpolation Search é mais eficiente em listas com intervalos uniformes, porque ele faz uma suposição sobre onde o número desejado pode estar.

# **3.	Explique como ele combina elementos do Jump Search e Binary Search.**
O Exponential Search combina o Jump Search e o Binary Search porque ele começa pulando intervalos em potências de 2 e, quando encontra o intervalo em que o número pode estar, aplica o Binary Search para localizar o elemento exato.

# **4.	Analise o desempenho do Exponential Search em listas muito grandes e pequenas.**
•	Listas pequenas: O overhead do Exponential Search pode torná-lo mais lento que o Binary Search.
•	Listas grandes: Ele é eficiente para encontrar rapidamente o intervalo onde o valor pode estar, especialmente útil em listas parcialmente indexadas ou dispersas.

# **5.	Explique como a escolha da sequência de intervalos afeta a eficiência do algoritmo. (shell sort)**
A determinação da sequência é crucial para definir a eficiência do algoritmo. Dependendo do intervalo utilizado, o algoritmo pode precisar fazer mais ou menos comparações.

# **6.  Explique o conceito de "dividir para conquistar" usado nesse algoritmo. (merge sort)**
"Dividir para conquistar" significa que o algoritmo divide o problema em subproblemas menores, que são resolvidos de forma recursiva, e depois as soluções são combinadas para formar a solução do problema original.

# **7.	Explique como os "baldes" são preenchidos e ordenados.**
No Bucket Sort, os elementos são divididos em subintervalos (baldes) para facilitar a ordenação. Após os baldes serem preenchidos, eles precisam de um algoritmo de ordenação interno para ordenar os elementos dentro de cada balde. Após, a ordenação os baldes são concatenados para exibir o resultado.

# **8.  Explique como o algoritmo lida com bases diferentes (ex.: base 10 e base 2). (radix sort)**
A base numérica (como base 10 ou base 2) afeta diretamente o processamento, pois, em base 10, a ordenação é feita dígito por dígito, enquanto em base 2, a ordenação é feita bit por bit, começando do dígito ou bit menos significativo até o mais significativo.

# **9.  Identifique situações em que o Ternary Search seria mais eficiente que o Binary Search.**
- Encontrar o máximo ou mínimo de uma função unimodal (crescente até um ponto e depois decrescente, ou o contrário).
- Dividir o espaço de busca em três partes, quando isso se adapta melhor ao problema.
- Refinar a busca de maneira mais precisa, dividindo o intervalo em três partes.

# **10.  Analise a complexidade de tempo e espaço de cada algoritmo de busca e ordenação listados.**

## Análise de Complexidade dos Algoritmos

### Comparação Geral

| Algoritmo        | Melhor Caso  | Médio Caso    | Pior Caso     | Espaço Adicional |
|-------------------|--------------|---------------|---------------|-------------------|
| Shell Sort        | O(n log n)  | O(n^(3/2))    | O(n^2)        | O(1)             |
| Merge Sort        | O(n log n)  | O(n log n)    | O(n log n)    | O(n)             |
| Quick Sort        | O(n log n)  | O(n log n)    | O(n^2)        | O(log n)         |
| Bucket Sort       | O(n + k)    | O(n + k)      | O(n^2)        | O(n + k)         |
| Radix Sort        | O(d * (n+b))| O(d * (n+b))  | O(d * (n+b))  | O(n + b)         |
| Busca Linear      | O(1)        | O(n)          | O(n)          | O(1)             |
| Busca Binária     | O(1)        | O(log n)      | O(log n)      | O(1) / O(log n)  |

### Observação
- \( n \): número de elementos na lista.
- \( k \): número de baldes no **Bucket Sort**.
- \( d \): número de dígitos no maior elemento no **Radix Sort**.
- \( b \): base numérica (ex.: 10 para decimais).

# **11.  Identifique quais algoritmos de ordenação da lista são estáveis e explique o que isso significa. Demonstre com exemplos.**
1.	Merge Sort
2.	Bubble Sort
3.	Insertion Sort
4.	Bucket Sort (quando a ordenação interna é estável)
5.	Radix Sort
   
Algoritmo Estável: Merge Sort
O Merge Sort é estável, o que significa que preserva a ordem dos elementos iguais.

Exemplo:
Antes: (4, 'a'), (4, 'c')
Depois: (4, 'a'), (4, 'c') (ordem preservada)

Algoritmo Não Estável: Selection Sort
O Selection Sort é não estável, podendo alterar a ordem de elementos iguais.

Exemplo:
Antes: (4, 'a'), (4, 'c')
Depois: (4, 'c'), (4, 'a') (ordem alterada)

