#Qual a desvantagem de usar deque em relação a usar lista??

import collections 

lista = collections.deque([1,2,3,4,5,6,7,2,42,43])

print(lista)

#coloca elemento no fim com O(1)
lista.append(3)
print(lista)

#coloca elemento no começo com O(1)
lista.appendleft(43)
print(lista)

#conta quantos de tal elementos 
print(lista.count(42))

#insere 69 na 4 posição
lista.insert(3,69)
print(lista)

#substitui o 2 elemento por 99
lista[1] = 99
print(lista)

#retorna o index do elemento do valor i até o valor j da lista
print(lista.index(69, 0, 10))

#pega os primeiros 4 elementos e joga para o final
lista.rotate(-4)
print(lista)

#reverte a lista
lista.reverse()
print(lista)