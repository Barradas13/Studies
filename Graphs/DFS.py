def bfsInicio(grafo):
    visitados = []
    cnt = 0

    for i in range(len(grafo)):
        visitados.append(-1)

    for i in range(len(visitados)):
        if visitados[i] == -1:
            bfsRec(grafo, visitados, cnt, i)

    return visitados

def bfsRec(grafo, visitados, ctn, v):
    ctn += 1
    visitados[v] = ctn
    for i in grafo[v]:
        if visitados[i] == -1:
            bfsRec(grafo, visitados, ctn, i)
    
    return visitados



def grafoConexoInicio(grafo):
    visitados = []

    for i in range(len(grafo)):
        visitados.append(-1)

    visitados[0] = 1

    for i in grafo[0]:
        visitados = grafoConexoRec(grafo, visitados, i)

    if visitados.count(-1) > 0:
        return False
    else:
        return True

def grafoConexoRec(grafo, visitados, v):
    visitados[v] = 1

    for i in grafo[v]:
        if visitados[i] == -1:
            grafoConexoRec(grafo, visitados, v)
    
    return visitados



def bipartidoInicio(grafo):
    visitados = []

    for i in range(len(grafo)):
        visitados.append(-1)

    return bipartidoRec(grafo, visitados, 0, 0)

def bipartidoRec(grafo, visitados, cor, v):
    visitados[v] = cor
    for i in grafo[v]:
        if visitados[i] == -1:
            return bipartidoRec(grafo, visitados, 1-cor, i)
        elif visitados[i] == cor:
            return False
    return True




def floodFill(matriz, corAtual, corPintar, i, j):
    matriz[i][j] = corPintar


    if i + 1 < len(matriz):
        if matriz[i+1][j] == corAtual:
            floodFill(matriz, corAtual, corPintar, i + 1, j)
    
    if i - 1 >= 0:
        if matriz[i-1][j] == corAtual:
            floodFill(matriz, corAtual, corPintar, i - 1, j)

    if j + 1 < len(matriz[0]):
        if matriz[i][j+1] == corAtual:
            floodFill(matriz, corAtual, corPintar, i, j + 1)
    
    if j - 1 >= 0:
        if matriz[i][j-1] == corAtual:
            floodFill(matriz, corAtual, corPintar, i , j- 1)
    
    return matriz

grafo = {0:(1,2,3),
         1:(0,),
         2:(0,),
         3:(0,),}

matriz = [[1,2,1],
          [2,2,2],
          [1,1,1]]

print(bfsInicio(grafo))
print(grafoConexoInicio(grafo))
print(floodFill(matriz, 2, 3, 0, 1))