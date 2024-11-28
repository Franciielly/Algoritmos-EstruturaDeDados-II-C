#**Questões**
**1.	Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.**
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
**2.	 Identifique casos em que o Interpolation Search é mais eficiente que o Binary Search.**
  O Interpolation Search é mais eficiente em listas com intervalos uniformes, porque ele faz uma suposição sobre onde o número desejado pode estar.
  
