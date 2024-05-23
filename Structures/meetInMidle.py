import itertools

def buscaBinaria(lista, numer):
    inicio = 0
    fim = len(lista)

    i = int(fim/2)
    
    while inicio < fim:

        if lista[i] < numer:
            inicio = i + 1
            i = int((inicio + fim) / 2)
        elif lista[i] > numer:
            fim = i - 1
            i = int((inicio + fim) / 2)
        else:
            return i
        
    if i >= len(lista):
        i = len(lista) - 1

    return i

def somaSubconjuntos(lista):
    resultado = [0 for i in lista]
    
    for i in range(len(lista)):
        for j in lista[i]:
            resultado[i] += j
    
    return resultado

def formaCombinacoes(lista):

    subconjuntos = []

    for i in range(len(lista) + 1):
        subconjuntos.extend(itertools.combinations(lista, i))

    return somaSubconjuntos(subconjuntos)



def metInMidle(lista, sum):
    mid = int(len(lista)/2)
    
    ans = float("-inf")

    left = formaCombinacoes(lista[0:mid])
    right = formaCombinacoes(lista[mid:])

    right.sort()

    for i in left:
        y = sum - i
        j = buscaBinaria(right, y)

        if right[j] + i > ans and (right[j] + i) <= sum:
            ans = right[j] + i

    return ans

lista = [5,3,1,75,4,3,1,2,3,4,1,5,6,8,52]
print(metInMidle(lista, 53))
