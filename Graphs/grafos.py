grafo = {
    1:[2,3],
    2:[5],
    3:[4],
    4:[1],
    5:[1],
}

def profundidade(grafo = grafo):
    cores = dict()
    pais = dict()
    distancias = dict()
    for i in grafo:
        cores[i] = "branco"
        pais[i] = None
        distancias[i] = 0
    for i in grafo:
        if cores[i] == "branco":
            cores[i] = "cinza"
            cores, distancias, pais = visitando_profundidade(i, grafo, cores, distancias, pais)

    print(distancias, cores, pais)

def visitando_profundidade(vertice, grafo, cores, distancias, pais):
    for i in grafo[vertice]:
        if cores[i] == "branco":
            distancias[i] = distancias[vertice] + 1
            pais[i] = vertice
            cores[i] = "cinza"
            cores, distancias, pais = visitando_profundidade(i, grafo, cores, distancias, pais)
        cores[vertice] = "preto"
    return cores, distancias, pais

import heapq

def largura(grafo, r):
    #cores = lista para definir o status do vértice, branco - ainda não passou; cinza - passando; preto - ja passou;
    cores = dict()
    #pais - lista para definir de onde vem para chegar;
    pais = dict()
    #distancia para chegar do r para o vertice desejado;
    distancias = dict()

    #lista vertices serve para definir quais nós estão sendo passados no momento;
    vertices = [r]
    heapq.heapify(vertices)

    #definindo as listas para retorno todas por enquanto sem distancia e pais e brancas (não foram passadas ainda)
    for i in grafo:
        cores[i] = "branco"
        pais[i] = None
        distancias[i] = None
    
    #se não tiver mais vértices para olhar acaba
    while len(vertices) > 0:
        #new vertices serve para definir quais vão ser os novos nós a se passar
        new_vertices = []
        heapq.heapify(new_vertices)
        distancias[r] = 0
        pais[r] = r
        
        #para cada aresta do vestice atual é visto qual é o lugar que chega, sua cor e dependendo desta se define resultados
        for i in range(len(vertices)):
            cores[vertices[0]] = "cinza"
            for j in grafo[vertices[0]]:
                if cores[j] == "branco":
                    pais[j] = vertices[0]
                    distancias[j] = distancias[vertices[0]] + 1
                    
                    heapq.heappush(new_vertices, j)
                    
            cores[vertices[0]] = "preto"
            heapq.heappop(vertices)

        vertices = new_vertices.copy()
    
    print(distancias, cores, pais)


largura(grafo, 1)
profundidade(grafo)