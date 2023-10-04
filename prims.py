"""
entrada:
n
nVezes com c, a, b (c = valor da aresta) (a = aresta 1) (b = aresta 2)

NAO DIRECIONADO

entrada exemplo:
5 4
10 1 2
32 0 1
24 3 4
12 4 0

grafo ficará:
[[(32, 1), (12, 4)], [(10, 2), (32, 0)], [(10, 1)], [(24, 4)], [(24, 3), (12, 0)]]
      v = 0                 v = 1          v = 2       v = 3          v = 4

a lista do grafo é representada por index = vertice, (c, b) c = valor da aresta, b = vertice que conecta
  
"""

import heapq

def ler_grafo(qtd_vertices, qtd_arestas):
    
    grafo = [[]*i for i in range(qtd_vertices)]
    
    for i in range(qtd_arestas):
        valores = list(map(int, input().split()))

        grafo[valores[1]].append((valores[0], valores[1], valores[2]))
        grafo[valores[2]].append((valores[0], valores[2], valores[1]))

    return grafo

def primAlgoritmo(grafo, raiz, n):
    mst = []
    valor = 0
    jaForam = [False for i in range(n)]
    
    while len(mst) < n - 1:
        vertices = grafo[raiz]
        heapq.heapify(vertices)

        jaForam[raiz] = True
        while True:
            valorC, verticeConectando, verticeLigado = heapq.heappop(vertices)

            if not jaForam[verticeLigado]:
                valor += valorC
                mst.append((valorC, verticeConectando, verticeLigado))
                jaForam[verticeLigado] = True

                for i in grafo[verticeLigado]:
                    if not jaForam[i[2]]:
                        heapq.heappush(vertices, i)

                break
        
    return mst, valor
        


v, a = map(int, input().split())

grafo = ler_grafo(v, a)

mst, valor = primAlgoritmo(grafo, 0, v)
print(valor)