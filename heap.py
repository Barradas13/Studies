import heapq
"""
arvore:
     2 
  12  12
32 45 _ _

em lista o filho de um node é nIndex * 2 ou nIndex * 2 + 1:
[2,12,12,32,45]
 1  2  3 4  5

considera apenas o primeiro valor, no caso de ter um heap de listas
[(2, 1, 3), (12, 1, 2), (12, 2, 3), (32, 4, 1), (45, 3, 4)] -> lista hepada
"""

lista = [(2, 1, 3),(45, 3, 4), (12, 2, 3),(32, 4, 1), (12, 1, 2)]

heapq.heapify(lista)

print(lista, end="\n\n")

#adicionar valor, considerando uma min heap
heapq.heappush(lista, (2, 2, 5))
print(lista, end="\n\n")

#pegando o primeiro valor da heap
primeiroValor = heapq.heappop(lista)
print(lista)
print(primeiroValor, end="\n\n")

#primeiro coloca um valor depois retorna o menor valor da lista
valorPuxado = heapq.heappushpop(lista, (1,5,4))
print(lista)
print(valorPuxado, end="\n\n")

#primeiro retorna o menor valor depois coloca um valor da lista
valorPuxado = heapq.heapreplace(lista, (1,5,4))
print(lista)
print(valorPuxado, end="\n\n")