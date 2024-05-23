import math
"""
Sparse table é um jeito muito mais rápido para computar o mínimo de querys em listas
a gnt utiliza o princípio do DIVIDIR PARA CONQUISTAR e com isso precomputamos todos os
possíveis valores iniciando em i e indo até 2^j

ou seja, Sparse table é uma matriz a qual o indíce i representa o início e o indice j 
representa até onde essa query vai e o valor será obviamente o mínimo dessa query i,j

"""


def criaSparceTable(lts):
    lista = []

    #K é o maximo valor de j
    #considerando que j não pode ultrapassar log n
    k = int(math.log2(len(lts)))

    #crio minha sparce table como uma matriz i por k + 1
    for i in range(len(lts)):
        lista.append([])
        for j in range(k + 1):
            lista[i].append(float("inf"))
    

    #todos os primeiros valores obviamente serão eles mesmos
    #pois para uma query de um valor o menos valor dela será ele mesmo
    for i in range(len(lista)):
        lista[i][0] = lts[i]


    #já que reutilizaremos os valores da lista para criar ela, passaremos
    #primeiro pelos i até o j e depois de passar por todos os i vamos mudar o j
    for j in range(1, k + 1):
        i = 0
        #o i deve ir até quando sua soma com 2^j for menos que n
        #pois vamos considerar as listas já prontas de [i] [j-1] e de [i + 2^j] [j -1]
        #comparamos desse modo para considerar um crescimento exponente
        #na primeira de 2 em 2, na segunda de 4 em 4, na terceira 8 em 8....
        while i + (1 << (j - 1)) < len(lista):
            #print(i, i + 2**(j-1))
            if lista[i][j - 1] <= lista[i + (1 << (j - 1))][j -1]:
                lista[i][j] = lista[i][j-1]
            else:
                lista[i][j] = lista[i + (1 << (j - 1))][j -1]
            i += 1
            
    return lista

#nosso range minimum query vai usar o K para o tamanho dos subgrupos
#o tamanho dos subgrupos virá de acordo com o tamanho inteiro do query que estamos
#verificando que é l2 - l1 + 1, K vai ser o log disso, já que separamos nosso sparce
#table todo em grupos de binários, agora verificaremos l1 até K, com isso ainda faltam elementos
#a serem comparados e a quantidade desses elementos é (tamanho da query) - 2^k e essa 
#quantidade de elementos que sobrou, nós vamos mover para frente e verificar até o subgrupo K
#por isso nós vamos comparar o subgrupo do i1 [K] e do [i2 - 2^(k-1)] mesmo que com
#isso alguns grupos se sobreescrevam
def RMQ(i1, i2, lista):
    tamanhoQuery = i2 - i1 + 1
    K = int(math.log2(tamanhoQuery))

    if lista[i1][K] > lista[tamanhoQuery - (1 << (K - 1))][K]:
        return lista[tamanhoQuery - (1 << (K - 1))][K]
    else:
        return lista[i1][K]
        

lista = [7,2,3,4,5,12,3,5,23, 4, 11, 12, 14,15,14,12]

sparceTable = criaSparceTable(lista)
print(RMQ(3, 7, sparceTable))
print(sparceTable)