import heapq

def ler_grafo(v, a):
    grafo = dict()

    for i in range(v):
        grafo[i] = []
    
    for i in range(a):
        #20 1 - 2, C v1 v2 (custo, vertice 1, vertice 2) NAO DIRECIONADO

        valores = list(map(int, input().split()))
        grafo[valores[1]].append((valores[0], valores[2]))
        grafo[valores[2]].append((valores[0], valores[1]))

    return grafo

def algoritmo_djikstra(grafo, origem):
    distancia = ["inf" for i in range(1, len(grafo) + 1)]
    pais = [None for i in range(len(grafo))]

    distancia[origem] = 0
    pais[origem] = origem

    candidatos = [origem]
    heapq.heapify(candidatos)

    while len(candidatos) > 0:
        u = heapq.heappop(candidatos)
        for i in grafo[u]:
            if distancia[i[1]] == "inf":
                distancia[i[1]] = distancia[u] + i[0]
                pais[i[1]] = u
                heapq.heappush(candidatos, i[1])
            elif distancia[i[1]] > distancia[u] + i[0]:
                distancia[i[1]] = distancia[u] + i[0]
                pais[i[1]] = u
                heapq.heappush(candidatos, i[1])

    return distancia, pais

v, a = map(int, input().split())

grafo = ler_grafo(v, a)
distancia, pais = algoritmo_djikstra(grafo, 1)
print(distancia, pais)