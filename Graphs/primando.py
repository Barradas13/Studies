import heapq

def prims(grafo, v = 0):
    pais = [-1 for i in range(len(grafo))]
    candidatos = [i for i in grafo[v]]
    ja_foi = [False for i in range(len(grafo))]

    valorMST = 0
    mst = []

    ja_foi[v] = True

    heapq.heapify(candidatos)
    
    while len(candidatos) > 0:
        valor, conectado, gancho = heapq.heappop(candidatos)
        
        if not ja_foi[conectado] and ja_foi[gancho]:
            
            mst.append([gancho, conectado, valor])
            valorMST += valor

            for i in grafo[conectado]:
                if not ja_foi[i[1]]:
                    heapq.heappush(candidatos, i)

            ja_foi[conectado] = True 

    return valorMST

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

print(prims(grafo, 0))
    