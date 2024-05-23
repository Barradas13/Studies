def lerGrafo(v, a):
    matriz = [[float("inf") for i in range(v)] for i in range(v)]

    for i in range(a):
            #entrada: v1 v2 c, onde v1 conecta v2 mas não o contrário
            v1, v2, c = map(int, input().split())

            matriz[v1 - 1][v2 - 1] = c

    return matriz

def floydMarshall(grafo):
    N = len(grafo)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])
                else:
                    grafo[i][j] = 0

    return grafo

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print("")

grafo = lerGrafo(4, 7)
imprimeMatriz(floydMarshall(grafo))
            