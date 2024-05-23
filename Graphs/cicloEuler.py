def insereAresta(grafo, u, a):
    try:
        grafo[u].append(a)
    except KeyError:
        grafo[u] = []
        grafo[u].append(a)

    try:
        grafo[a].append(u)
    except KeyError:
        grafo[a] = []
        grafo[a].append(u)

    return grafo

def removeAresta(grafo, u, a):
    grafo[u].remove(a)
    grafo[a].remove(u)

    return grafo

def DFSInicio(grafo, u):
    validos = [False for i in range(len(grafo))]

    validos = DFS(grafo, u, validos)

    for i in validos:
        if i == False:
            return False
        
    return True

def DFS(grafo, u, validos):
    validos[u] = True
    for i in grafo[u]:
        if not validos[i]:
            DFS(grafo, i, validos)
    
    return validos

def verificaSeArestaValida(grafo, u, a):
    if len(grafo[u]) == 1:
        return True
    else:

        c1 = DFSInicio(grafo, u)

        removeAresta(grafo, u, a)

        c2 = DFSInicio(grafo, u)

        insereAresta(grafo, u, a)

        if c1 == c2:
            return True
        else:
            return False


def euler(grafo, inicio, res):
    res.append(inicio)
    for i in grafo[inicio]:
        if verificaSeArestaValida(grafo, inicio, i):
            removeAresta(grafo, inicio, i)
            #print(f'{inicio} - {i}', end="/")
            euler(grafo, i, res)

    return res

def verificaSeTemCiclo(grafo):
    grausV = []
    impares = 0

    for i in grafo:
        grausV.append(len(grafo[i]))
        if len(grafo[i]) % 2 != 0 :
            impares += 1

    if impares > 2:
        return 0
    elif impares == 2:
        return 1
    else:
        return 2
    


if __name__ == "__main__":
    graph = {}

    insereAresta(graph, 0, 1)
    insereAresta(graph, 1, 2)
    insereAresta(graph, 2, 3)
    insereAresta(graph, 3, 4)
    insereAresta(graph, 4, 0)
    insereAresta(graph, 4, 1)
    insereAresta(graph, 4, 2)
    insereAresta(graph, 3, 1)



    valida = verificaSeTemCiclo(graph)

    if valida == 0:
        print("Grafo sem ciclo de euler")
    elif valida == 1:
        print("Grafo tem caminho de euler")

        for i in graph:
            if len(graph[i]) % 2 != 0:
                print(euler(graph, i, []))
    else:
        print("Grafo tem ciclo de euler")
        print(euler(graph, 0, []))