"""
ARVORE DE INDEXAÇÃO BINÁRIA (BIT) -> Para somar valores de uma lista e poder alterá-los em tempo O(N(log(N))) - p/construir
e log(N) -> somar log(N) -> alterar valores

funciona por conta dos números binários, dividimos com esses a responsabilidade de cuidar não somente de seu prop valor
mas muitas vezes da seu valor e dos outros, para que assim façamos verificações e alterações mais rápido

DIVIDA PARA CONQUISTAR

LSB (Least Significant Bit) -> é o bit mais à direita de um número; encontramos com a formula n & -n

A árvore não irá guardar apenas o valor próprio, mas também de seus LSB, ou seja, o índice 6 vai guardar além do valor
no indice 6 da lista o valor do índice abaixo dele, pois 6 = 0110(2) -> LSB = 10(2) = 2, ou seja, os números guardarão
a quantidade de seus LSB números, por exemplo 8 = 1000(2) -> LSB = 1000(2) = 8 irá guardar 8 números abaixo dele

"""


#A soma até um valor é a (quantidade desse valor) na árvore + a (quantidade do valor - LSB) na árvore.
def soma(arvore, i):
    soma = 0
    
    while i > 0:
        soma += arvore[(i & -i)]
        i -= i & -i
    
    return soma

#Quando mudamos, apenas precisamos alterar os valores responsáveis pelo índice que está mudando, ou seja, os LSB do valor somados
def mudanca(arvore, i, mudanca):
    arvore[i] += mudanca
    i += i & -i

    while i < len(arvore):
        arvore[i] += mudanca
        i += i & -i

    return arvore


#para construir a árvore utilizaremos dos valores já colocados na lista, sempre necessariamente um valor quando chega aq é pq ele vai cuidar
#de pelo menos ele + o de baixo dele, e o menor número possível q ele cuidará vai ser ele - o LSB dele, portanto se por acaso ele for
#potencia de 2 vai cuidar de todos abaixo dele já que o menor nmr possível será 0.
#por aproveitarmos o que já fizemos vamos tirando o LSB do número e pegando os que já foram pre-computados 

def somaConstruindo(arvore, i):
    soma = arvore[i-1]
    minI = i - (i & -i)
    i -= 1
    i -= (i & -i)

    while i > minI:
        soma += arvore[i]
        i -= (i & -i)
    
    return soma

def constroiBIT(lista):
    arvore = [0 for i in range(len(lista))]

    for i in range(1, len(lista)):
        lsb = i & -i
        
        if lsb == 1:
            arvore[i] = lista[i]
        else:
            arvore[i] = lista[i] + somaConstruindo(arvore, i)
            
    return arvore

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

BIT = constroiBIT(lista)

print(BIT)

BIT = mudanca(BIT, 1, float("inf"))
print(BIT)