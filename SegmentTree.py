"""
Vai DIVIDIR PARA CONQUISTAR

divide em grupos com tamanhos log2 n
cada grupo vai ter um valor de soma = a soma dos seus de baixo
e um valor minimo = o menor valor dentro da query
com isso podemos fazer verificações de min e soma de querys em log n tempo

a vantagem do seg tree em relação a estruturas como o sparce table é que ele
pode alterar valor em um range (pode mudar uma query inteira) em log n tempo
portanto ele é muito bom para quando eu quero ficar alterando muitos valores

"""


class SegmentTree():

    #primeiro indice da sublista, ultimo indice da sublista
    leftmost = 0
    rightmost = 0

    #as suas crianças, que tmb são segment trees
    lChild = None
    rChild = None

    #a soma e o menor valor dentro da seg
    sum = 0
    min = float("inf")

    #a lista dos valores
    a = []


    def __init__(self, leftmost, rightmost, a) -> None:
 
        self.leftmost = leftmost
        self.rightmost = rightmost
        
        if leftmost == rightmost:
            #its a leaf -> só colocar os valores normalmente, já que não tem com oq comparar
            self.sum = a[leftmost]
            self.min = a[leftmost]
        else:
            #divide em 2 subgrupos
            mid = int((leftmost + rightmost)/2)

            self.lChild = SegmentTree(leftmost, mid, a)
            self.rChild = SegmentTree(mid + 1, rightmost, a)
            
            #chama o recalc e o calcmin que calcularão o min e a soma dos subgrupos abaixo
            self.sum = self.recalc()
            self.min = self.calcMin()

    def recalc(self):
        if self.leftmost == self.rightmost:
            #se for folha não precisa calcular nada já q ja foi calculado no começo da função de construção ou de alteração
            return
        else:
            #se não for folha vai chamar a soma dos seus dois filhos, que são a soma dos subgrupos até que eles virem folhas e retorne a soma de tudo normalmente
            return self.lChild.sum + self.rChild.sum
        
    def calcMin(self):
        if self.leftmost == self.rightmost:
            #se for folha é ela mesma
            return self.sum
        else:
            #se não for folha vai indo e verificando os menores valores dos subgrupos dela
            return min(self.lChild.calcMin(), self.rChild.calcMin())
                
    def pointUpdate(self, index, value):
        #se for folha troca normalmente
        if self.leftmost == self.rightmost:
            self.sum = value
            self.min = value
        else:
            #se o index for do subgrupo da esquerda troca da esquerda passando agr como seg o filho da esquerda
            if self.lChild.rightmost >= index:
                self.lChild.pointUpdate(index, value)
            else:
            #se o index for do subgrupo da direita troca da direita passando agr como seg o filho da direita
                self.rChild.pointUpdate(index, value)
            
            #recalcula tudo pq tlg ne
            self.sum = self.recalc()
            self.min = self.calcMin()

        
    def RMQ(self, lQuery, rQuery, lAtual, rAtual):

        if lAtual >= lQuery and rAtual <= rQuery:
            #its totaly inside it -> então retorna o min q já é calculado
            return self.min
            
        elif lAtual > rQuery or rAtual < lQuery:
            #its outside -> retorna inf pq não é considerado no min
            return float("inf")
        else:
            #its in parts inside -> vai dividir e pegar o min dessas divisões
            mid = int((lAtual + rAtual)/2)
            return min(self.lChild.RMQ(lQuery, rQuery, lAtual, mid), self.rChild.RMQ(lQuery, rQuery, mid + 1, rAtual))
    
    def querySum(self, lQuery, rQuery, lAtual, rAtual):
        #mesmo que o rmq porem agr somando e quando nao ta dentro manda 0 pra nao somar
        if lAtual >= lQuery and rAtual <= rQuery:
            return self.sum
        
        elif lAtual > rQuery or rAtual < lQuery:
            return 0
        
        else:
            return self.lChild.querySum(lQuery, rQuery, self.lChild.leftmost, self.lChild.rightmost) + self.rChild.querySum(lQuery, rQuery, self.rChild.leftmost, self.rChild.rightmost) 


lista = [1,2,3,4,5,6,7,8]
segment = SegmentTree(0, len(lista) -1, lista)

print(segment.sum)   
segment.pointUpdate(3, -1)

print(segment.RMQ(2, 5, 0, len(lista)-1))
print(segment.min)


print(segment.querySum(3, 6, 0, len(lista) -1))
print(segment.sum)