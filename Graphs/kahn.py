def kahn(grafo):
    ordenacao = []
    indegree = {i:0 for i in range(len(grafo))}
    removidos = [False for i in range(len(grafo))]

    candidatos = []

    for i in grafo:
        for j in grafo[i]:
            indegree[j] += 1

    for i in indegree:
        if indegree[i] == 0:
            candidatos.append(i)

    while len(candidatos) > 0:
        u = candidatos.pop()
        ordenacao.append(u)
        for j in grafo[u]:
            indegree[j] -= 1

            if indegree[j] == 0 and not removidos[j]:
                candidatos.append(j)
                removidos[j] = True

            

    return ordenacao


#O 1 depende do 0, o 2 depende do 1 e do 0 
grafo = {0:[], 1:[], 2:[1, 0]}
print(kahn(grafo))