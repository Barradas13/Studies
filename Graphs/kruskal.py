def kruscal(grafo):
    ja_foi = [False for i in range(len(grafo))]

    candidatos = []

    for i in grafo:
        for j in grafo[i]:
            candidatos.append(j)

    candidatos.sort()

    mst = []
    valorMST = 0

    while len(mst) < len(grafo) - 1:
        valor, conectando, gancho = candidatos.pop(0)
        print(mst)
        if not ja_foi[conectando] or not ja_foi[gancho]:
            ja_foi[conectando] = True
            ja_foi[gancho] = True
            valorMST += valor
            mst.append([conectando, gancho, valor])

    return mst 


grafo = {0:[[10,1], [1, 2], [4, 3]], 
         1:[[10, 0], [3, 2], [0, 4]], 
         2:[[1, 0], [3,1], [2,3], [8,5]], 
         3:[[4, 0], [2,2], [2,5],[7,6]], 
         4:[[0,1],[1,5],[8,7],], 
         5:[[8,2],[2,3],[6,6],[9,7],[1,4]],
         6:[[7,3],[6,5],[12,7],],
         7:[[8,4],[12,6]]}

for i in range(len(grafo)):
    for j in range(len(grafo[i])):
        grafo[i][j].append(i)

print(kruscal(grafo))