def larguraSearch(grafo, v):
    distancia = []
    pais = []

    cnt = 1

    for i in range(len(grafo)):
        distancia.append(-1)
        pais.append(-1)

    vertices = [v]
    distancia[v] = 0
    pais[v] = v
    
    while len(vertices) > 0:
        u = vertices.pop(0)

        for i in grafo[u]:
            if distancia[i] == -1:
                vertices.append(i)
                distancia[i] = cnt
                pais[i] = u
        
        cnt += 1

    return distancia, pais

grafo = {0:(1,2,3),
         1:(0,),
         2:(0,),
         3:(0,),}

print(larguraSearch(grafo, 0))