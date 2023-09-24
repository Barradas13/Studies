grafo = {
    1:[2],
    2:[5],
    3:[1],
    4:[3],
    5:[],
}

def profundidade(destino, origem, grafo = grafo):
    achou = False
    if origem[-1] == destino:
        achou = True
    else:
        for i in grafo[origem[-1]]:
            if i not in origem:
                nova_origem = origem.copy()
                nova_origem.append(i)
                if profundidade(destino, nova_origem, grafo):
                    achou = True
    return achou

def largura(destino, origem, grafo = grafo):
    achou = False
    if destino in origem:
        achou = True
    else:
        nova_origem = set()
        for i in origem:
            for j in grafo[i]:
                nova_origem.add(j) 
        if nova_origem != origem:
            if largura(destino, nova_origem, grafo):
                achou = True

    return achou

print(profundidade(1, [5]))
print(largura(1, {5}))