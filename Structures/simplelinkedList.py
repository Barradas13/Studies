#Linked list -> elementos soltos com ponteiros
# simple -> Só pra frente
# double -> frente e tras

# |head| -> |2| --> |3| -> null

class ElementoSimples():

    def __init__(self, data) -> None:
        self.valor = data    
        self.ponteiro = None

class SimpleLinkedList():
    def __init__(self) -> None:
        self.head = ElementoSimples(None)
        self.size = 0

    def addInicio(self, data):
        if self.head.valor == None:
            self.head.valor = data
        else:
            atual = ElementoSimples(data)
            atual.ponteiro = self.head
            self.head = atual
        self.size += 1

    def addIndex(self, data, index):
        if index == 0:
            self.addInicio(data)
        else:
            elementoAdd = ElementoSimples(data)
            i = 0
            atual = self.head

            while i != index -1 and atual.ponteiro != None:
                atual = atual.ponteiro
                i += 1

            #encontrou
            if atual != None:
                antigoPonteiro = atual.ponteiro
                atual.ponteiro = elementoAdd
                elementoAdd.ponteiro = antigoPonteiro
            else:
                print('Index não listado')

        self.size += 1

    def removeIndex(self, index):
        if index == 0:
            self.head = self.head.ponteiro
        else:
            i = 1
            atual = self.head.ponteiro
            while i != index -1 and atual.ponteiro != None:
                atual = atual.ponteiro 
                i += 1
            
            atual.ponteiro = atual.ponteiro.ponteiro
            atual.ponteiro.ponteiro = None

        self.size -= 1

    def inserirFinal(self, data):
        atual = self.head

        while atual.ponteiro != None:
            atual = atual.ponteiro
        
        novo = ElementoSimples(data)

        atual.ponteiro = novo

        self.size += 1

    def print(self):
        atual = self.head
        while atual.ponteiro != None:
            print(atual.valor, end=" ")
            atual = atual.ponteiro
        print(atual.valor)

    def noIndex(self, index):
        atual = self.head

        for i in range(index):
            atual = atual.ponteiro

        print(atual.valor)
        
lista = SimpleLinkedList()
lista.addInicio("A")
lista.addInicio("B")
lista.addInicio("C")

lista.addIndex("D", 2)

lista.noIndex(3)
lista.print()
print(lista.size)
    
    