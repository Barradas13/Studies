def minMax1(lista):
    min = lista[0]
    max = lista[0]

    for i in lista:
        if i < min:
            min = i
        if i > max:
            max = i
    
    return min, max
    
def minMax2(lista):
    min = lista[0]
    max = lista[0]

    for i in lista:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max
    

def minMax3(lista):
    if lista[0] > lista[1]:
        min = lista[1]
        max = lista[0]
    else:
        min = lista[0]
        max = lista[1]

    i = 0

    while i < len(lista):
        if len(lista) % 2 > 0:
            lista.append(lista[0])
        if lista[i] > lista[i + 1]:
            if lista[i] > max:
                max = lista[i]
            elif lista[i + 1] > max:
                max = lista[i + 1]
        else:
            if lista[i] < min:
                min = lista[i]
            elif lista[i + 1] < min:
                min = lista[i + 1]

        i += 2

    return min, max
    

lista = [5,4,3,2,1]
