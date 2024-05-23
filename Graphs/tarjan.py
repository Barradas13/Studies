from collections import defaultdict

class Graph():

    def __init__(self, vertices) -> None:
        self.V = vertices
        self.disc = [-1] * self.V
        self.low = [-1] * self.V
        self.stackMember = [False] * self.V
        self.time = 0
        self.st = []
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def tarjanRec(self, u):
        
        self.low[u] = self.time
        self.disc[u] = self.time
        self.time += 1
        self.stackMember[u] = True
        self.st.append(u)

        for v in self.graph[u]:

            if self.disc[v] == -1:
                self.tarjanRec(v)
                self.low[u] = min(self.low[u], self.low[v])
                

            elif self.stackMember[v]:

                self.low[u] = min(self.low[u], self.disc[v])

        
        w = -1  # To store stack extracted vertices
        if self.low[u] == self.disc[u]:
            while w != u:
                w = self.st.pop()
                print(w, end=" ")
                self.stackMember[w] = False
 
            print()

    def tarjan(self):
        for i in range(self.V):
            if self.disc[i] == -1:
                self.tarjanRec(i)


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("SSC in first graph ")
g1.tarjan()
print(g1.low)
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nSSC in second graph ")
g2.tarjan()
 
 
g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nSSC in third graph ")
g3.tarjan()
 
g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print("\nSSC in fourth graph ")
g4.tarjan()
 
 
g5 = Graph(5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print("\nSSC in fifth graph ")
g5.tarjan()
 