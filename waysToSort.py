#Ordenação em n^2 INSERTION SORT
def insertion(lista):
    for i in range(1, len(lista)):
        chave = lista[i]

        j = i - 1

        while j >= 0 and lista[j] > chave:
            #jogo o numero de trás para frente
            lista[j+1] = lista[j]
            j -= 1

        lista[j+ 1] = chave

def merge(l1, l2):
    i = 0
    j = 0

    result = []

    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            result.append(l2[j])
            j += 1
        else:
            result.append(l1[i])
            i += 1
    
    while i < len(l1):
        result.append(l1[i])
        i += 1

    while j < len(l2):
        result.append(l2[j])
        j += 1 

    return result

def mergeSort(l):
    if len(l) <= 1:
        return l
    else:
        mid = int(len(l) / 2)

        esquerda = mergeSort(l[0:mid])
        direita = mergeSort(l[mid:])

    return merge(esquerda, direita)


def countSort(l):
    max = l[0]
    for i in l:
        if max < i:
            max = i

    B = [0 for i in range(max)]

    for i in range(len(l)):
        B[l[i] - 1] += 1

    for i in range(1, len(B)):
        B[i] += B[i-1]

    C = [0 for i in range(len(l))]

    for i in range(len(l), 0, -1):
        C[B[l[i - 1] - 1] - 1] = l[i - 1]
        B[l[i - 1] - 1] -= 1

    return C

def twoPointers(x, array):
    i = 0
    j = len(array) -1
    
    while i < j:
        
        if array[i] + array[j] == x:
            return i, j
        elif array[i] + array[j] < x:
            i += 1
        else:
            j -= 1

    return None

lista = [5,12,4,4,2,14,2,2,4,1,2,4,21,132]

print(twoPointers(16, countSort(lista)))
print(countSort(lista))