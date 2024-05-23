from collections import defaultdict

class Arvore():

    def __init__(self, v, a) -> None:
        self.leafs = v
        self.branches = defaultdict(list)

    def addBranch(self, u, v):
        self.branches[u].append(v)
        self.branches[v].append(u)

    def BFS(self, raiz, visited, dist, pais):

        dist[raiz] = dist[pais[raiz]] + 1
        visited[raiz] = True
        for i in self.branches[raiz]:
            if not visited[i]:
                pais[i] = raiz
                self.BFS(i, visited, dist, pais)

        return dist, pais
    
    def findDiameter(self, raiz):

        dist, pais = self.BFS(raiz, [False] * self.leafs, [-1]*self.leafs, [-1]*self.leafs)
        
        max = -1
        v = -1
        
        for i in range(len(dist)):
            
            if int(dist[i]) > max:
                max = dist[i]
                v = i
        
        dist, pais = self.BFS(v, [False] * self.leafs, [-1]*self.leafs, [-1]*self.leafs)
    
        max = -1
        u = -1
        for i in range(len(dist)):
            if dist[i] > max:
                max = dist[i]
                u = i
                
        return u, v
    
    def findCenter(self):
        u, v = self.findDiameter(1)

        c = u
        atual = u
        mx = float("inf")



if __name__ == "__main__":
    arvore = Arvore(9, 8)

    arvore.addBranch(0, 3)
    arvore.addBranch(1, 3)
    arvore.addBranch(1, 2)
    arvore.addBranch(5, 4)
    arvore.addBranch(5, 6)
    arvore.addBranch(6, 7)
    arvore.addBranch(7, 8)
    arvore.addBranch(5, 3)

    print(arvore.findDiameter(0))
