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

class MergeSortTree():

    leftmost = 0
    rightmost = 0

    lChild = None
    rChild = None

    a = []

    def __init__(self, a, inicio, fim):
        print(inicio, fim, a)
        #its a branch
        if len(a) > 1:
            midCriaAgr = int(len(a)/2)

            self.leftmost = inicio
            self.rightmost = fim

            mid = int((inicio + fim)/2)

            self.lChild = MergeSortTree(a[0:midCriaAgr], inicio, mid)
            self.rChild = MergeSortTree(a[midCriaAgr:], mid + 1, fim)

            self.a = merge(self.lChild.a, self.rChild.a)
        else:
            self.rightmost = inicio
            self.leftmost = inicio
            self.a = a

    def menorQemQuery(self, i, j, num):
        #estou dentro de tudo
        if self.leftmost >= i and self.rightmost <= j:
            return

lista = [1,2,3,4,6,2,7,8]
arvore = MergeSortTree(lista, 0, len(lista) - 1)

print(arvore.a)