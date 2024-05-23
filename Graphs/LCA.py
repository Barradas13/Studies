import math

def ler_arvore(v, a):
    grafo = {i:[] for i in range(1, v + 1)}

    for i in a:
        v1, v2 = i[0], i[1]

        grafo[v1].append(v2)

    return grafo

def binary_lifting(grafo, n, LOG):
    ancestrais = [[-1 for i in range(LOG)] for j in range(n + 1)]

    for i in grafo:
        for j in grafo[i]:
            ancestrais[j][0] = i

    for i in range(1, n + 1):
        for j in range(1, LOG):
            if ancestrais[i][j - 1] != -1:
                ancestrais[i][j] = ancestrais[ancestrais[i][j-1]][j-1]
                
    return ancestrais

def BFS(tree, n, raiz = 1):
    ja_foram = [False for i in range(n + 1)]
    nivel = [-1 for i in range(n + 1)]
    pais = [-1 for i in range(n + 1)]

    pais[raiz] = raiz
    nivel[raiz] = 0

    candidatos = [raiz]

    while len(candidatos) > 0:
        u = candidatos.pop(0)

        for i in tree[u]:
            if not ja_foram[i]:
                pais[i] = u
                nivel[i] = nivel[u] + 1

                candidatos.append(i)

        ja_foram[u] = True
        
    print(nivel, pais)
    return nivel


def LCA(x, y, ancestrais, nivel, LOG):

    if nivel[x] < nivel[y]:
        x, y = y, x
    
    #coloco os dois no mesmo nível
    if nivel[x] > nivel[y]:
        for i in range(LOG - 1, -1, -1):
            if nivel[x] - (1 << i) >= nivel[y]:
                x = ancestrais[x][i] 
                
    #se os dois ja forem iguais quer dizer que ja são o proprio LCA
    if x == y:
        return x
    
    #agora, vamos pegar o menos nível em comum deles que não iguale seus valores
    for i in range(LOG-1,-1,-1):
        if ancestrais[x][i] != ancestrais[y][i] and ancestrais[x][i] != -1:
            x = ancestrais[x][i]
            y = ancestrais[y][i]
            
    return ancestrais[x][0]


tree = ler_arvore(5, [[1,2],[1,3],[3,4],[3,5]])
n = len(tree)
LOG = int(math.log2(n))
ancestrais = binary_lifting(tree, n, LOG)
nivel = BFS(tree, n)
print(LCA(5,2, ancestrais, nivel, LOG))