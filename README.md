# **Questões:**
# **1.	Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.**
A lista precisa estar ordenada, pois o Binary Search elimina um lado. Se o número desejado for maior que o do meio, ele elimina toda a parte esquerda. Dito isso, em uma lista desordenada, pode ser que o número desejado esteja no lado que será eliminado.
Ex: [1,2,3,4,5] – lista ordenada
Número desejado = 4 
Meio = 3 
- elimina toda esquerda (menores que meio)
- meio = 4
Elemento encontrado!
Ex  : [4,1,2,3,4] – lista desordenada
Número desejado = 4
Meio = 2
-elimina toda esquerda
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


Aqui está uma análise detalhada da complexidade de tempo e espaço dos algoritmos de busca e ordenação listados no seu código:

1. Shell Sort
Complexidade de Tempo:
Melhor caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) (depende do gap sequence, com sequências otimizadas como Hibbard ou Knuth).
Médio caso: 
𝑂
(
𝑛
3
/
2
)
O(n 
3/2
 ) (usando gap sequences típicas).
Pior caso: 
𝑂
(
𝑛
2
)
O(n 
2
 ) (para gap sequence ineficiente, como divisão por 2).
Complexidade de Espaço:
Espaço adicional: 
𝑂
(
1
)
O(1) (in-place, usa trocas diretas na lista).
2. Merge Sort
Complexidade de Tempo:
Melhor caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) (independente da ordem dos elementos).
Médio caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
Pior caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
Complexidade de Espaço:
Espaço adicional: 
𝑂
(
𝑛
)
O(n) (necessário para arrays auxiliares na fusão).
3. Quick Sort
Complexidade de Tempo:
Melhor caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) (quando o pivô divide uniformemente os subarrays).
Médio caso: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).
Pior caso: 
𝑂
(
𝑛
2
)
O(n 
2
 ) (ocorre quando o pivô é o menor ou maior elemento, criando partições desbalanceadas).
Complexidade de Espaço:
Espaço adicional:
𝑂
(
log
⁡
𝑛
)
O(logn) (para a pilha de recursão, em média).
𝑂
(
𝑛
)
O(n) (no pior caso, em recursão desbalanceada).
4. Bucket Sort
Complexidade de Tempo:
Melhor caso: 
𝑂
(
𝑛
+
𝑘
)
O(n+k), onde 
𝑘
k é o número de baldes.
Médio caso: 
𝑂
(
𝑛
+
𝑘
)
O(n+k).
Pior caso: 
𝑂
(
𝑛
2
)
O(n 
2
 ) (se todos os elementos forem mapeados para o mesmo balde e precisar de uma ordenação interna).
Complexidade de Espaço:
Espaço adicional: 
𝑂
(
𝑛
+
𝑘
)
O(n+k) (espaço para os baldes).
5. Radix Sort
Complexidade de Tempo:
Melhor caso: 
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b)), onde:
𝑑
d é o número de dígitos no maior número.
𝑏
b é a base (ex.: 10 para números decimais).
Médio caso: 
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b)).
Pior caso: 
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b)).
Complexidade de Espaço:
Espaço adicional: 
𝑂
(
𝑛
+
𝑏
)
O(n+b) (espaço para os buckets e arrays auxiliares).
6. Busca Linear (Não implementada, mas relevante)
Complexidade de Tempo:
Melhor caso: 
𝑂
(
1
)
O(1) (encontrar o elemento na primeira posição).
Pior caso: 
𝑂
(
𝑛
)
O(n) (elemento não encontrado ou na última posição).
Médio caso: 
𝑂
(
𝑛
)
O(n).
Complexidade de Espaço:
Espaço adicional: 
𝑂
(
1
)
O(1) (não utiliza memória extra).
7. Busca Binária (Não implementada, mas relevante)
Complexidade de Tempo:
Melhor caso: 
𝑂
(
1
)
O(1) (encontrar o elemento no meio da lista).
Médio caso: 
𝑂
(
log
⁡
𝑛
)
O(logn) (a lista é dividida ao meio em cada iteração).
Pior caso: 
𝑂
(
log
⁡
𝑛
)
O(logn).
Complexidade de Espaço:
Espaço adicional:
𝑂
(
1
)
O(1) (iterativa).
𝑂
(
log
⁡
𝑛
)
O(logn) (recursiva, devido à pilha de chamadas).
Comparação Geral
Algoritmo	Melhor Caso	Médio Caso	Pior Caso	Espaço Adicional
Shell Sort	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
3
/
2
)
O(n 
3/2
 )	
𝑂
(
𝑛
2
)
O(n 
2
 )	
𝑂
(
1
)
O(1)
Merge Sort	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
)
O(n)
Quick Sort	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
2
)
O(n 
2
 )	
𝑂
(
log
⁡
𝑛
)
O(logn)
Bucket Sort	
𝑂
(
𝑛
+
𝑘
)
O(n+k)	
𝑂
(
𝑛
+
𝑘
)
O(n+k)	
𝑂
(
𝑛
2
)
O(n 
2
 )	
𝑂
(
𝑛
+
𝑘
)
O(n+k)
Radix Sort	
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b))	
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b))	
𝑂
(
𝑑
⋅
(
𝑛
+
𝑏
)
)
O(d⋅(n+b))	
𝑂
(
𝑛
+
𝑏
)
O(n+b)
Busca Linear	
𝑂
(
1
)
O(1)	
𝑂
(
𝑛
)
O(n)	
𝑂
(
𝑛
)
O(n)	
𝑂
(
1
)
O(1)
Busca Binária	
𝑂
(
1
)
O(1)	
𝑂
(
log
⁡
𝑛
)
O(logn)	
𝑂
(
log
⁡
𝑛
)
O(logn)	
𝑂
(
1
)
O(1)/
𝑂
(
log
⁡
𝑛
)
O(logn)

