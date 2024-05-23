import heapq

def djikstra(grafo, s):
    pais = []
    dist = []
    candidatos = []
    maduros = []

    for i in range(len(grafo)):
        pais.append(-1)
        dist.append(float("inf"))
        maduros.append(False)
    
    pais[s] = s
    dist[s] = 0

    candidatos = [[s, 0]]

    while len(candidatos) > 0:
  
        u = heapq.heappop(candidatos)[1]

        if not maduros[u]:
            for i in grafo[u]:
                v = i[1]
                c = i[0]

                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    pais[v] = u

                    add = [dist[v], v]

                    heapq.heappush(candidatos, add)
            maduros[u] = True

    return dist, pais

grafo = {0:[[70, 2], [50, 3], [30, 4]], 
         1:[[30,2],], 
         2:[[10,4],], 
         3:[[10,4], [20,5]], 
         4:[[0, 1],[30, 5]], 
         5:[[50, 1],]}

print(djikstra(grafo, 0))