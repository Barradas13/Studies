
"""THIS ENTIRE CODE HAVE THE CODES THAT I DID FOR DOING MATH OPERATIONS, SUCH AS MODULE EXPONENTIAL
    MATRIZ OPERATION (MULTIPLICATION...), FAST EXPONENTIAL, LAPLACE ALGORITHM AND A LOT MORE
    IT IS DIVIDED INTO PARTS AS YOU CAN SEE ON THE SUMARRY"""

"""
SUMARRY:
1) MODULATION MATH  -> LINE 14
2) PRIME NUMBERS AND MDC  -> LINE 71
3) MATRIZES OPERATIONS  -> LINE 103
4) LA PLACE ALGORITHM  -> LINE 182

"""

#CODE RELATED TO MODULATION MATH 
def modularizando( a, c):
    q = int(a/c)
    r = (q * c) - a

    if r < 0:
        r = -1 * r

    return r

def somaModulos(a, b, c):
    #(a + b) % c == a % c + b % c
    return modularizando(a + b, c)

def subtraiModulos(a, b, c):
    #(a + b) % c == a % c + b % c
    return modularizando(a - b, c)
    
def multiplicacaoModulos(a,b,c):
    return modularizando(a * b, c)

def transformaNumeroBinario(n):
    binario = ""
    
    while n >= 1:
        resto = modularizando(n, 2)
        #print(resto)
        if resto == 0:
            binario = '0' + binario
        else:
            binario = '1' + binario
        n = int(n/ 2)

    return binario

def exponenciacaoModulos(a,b,c):
    binario = transformaNumeroBinario(b)
    
    #Agora dividimos para conquistar, fazemos o valor de cada mod da exponenciação por partes
    #E MULTIPLICAMOS E ENTÃO SOMENTE FAZEMOS O MOD FINAL

    lista = [0 for i in binario]

    for i in range(len(binario) -1, -1, -1):
        if i == len(binario) -1:
            lista[i] = modularizando(a, c)
        else:
            lista[i] = multiplicacaoModulos(lista[i + 1], lista[i + 1], c)

    resultado = 1

    for i in range(len(binario)):
        if binario[i] == 1:
            resultado *= multiplicacaoModulos(binario[i], c)

    return modularizando(resultado, c)

#PRIMES NUMBERS AND MDC
def euclidiano( n, m):
    while n > 0 and m > 0:
        n, m = max(n, m), min(n, m)
        n, m = modularizando(n, m), m
    return max(n, m)

def nPrimo( n):
    i = 2
    while i * i < n: 
        if(modularizando(n, i) == 0):
            return False
        i += 1
    return True

def qtdPrimos( n):
    ja_foi = [False for i in range(n)]
    soma = 0
    for i in range(2, n):
        if not ja_foi[i - 1]:
            j = i * 2
            while j <= n:
                ja_foi[j - 1] = True
                j = i + j
    for i in ja_foi[1:]:
        if not i:
            soma += 1
            
    return soma



#CODE RELATED TO OPERATIONS IN MATRIZ
def criaMatriz(n, m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(0)

    return matriz

def imprimeMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

def multiplicaVetores(vet1, vet2):
    soma = 0

    for i in range(len(vet1)):
        soma += vet1[i] * vet2[i]

    return soma

def transpostaMatriz(matriz):
    matrizReturn = criaMatriz(len(matriz[0]), len(matriz))

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matrizReturn[i][j] = matriz[j][i]

    return matrizReturn

def multiplicaMatriz(mat1, mat2):
    mat2T = transpostaMatriz(mat2)
    mat3 = criaMatriz(len(mat1), len(mat2T))

    j = 0
    i = 0

    while j < len(mat1) and i != len(mat2[0]):
        mat3[i][j] = multiplicaVetores(mat1[i], mat2T[j])
        if i + 1 >= len(mat1):
            i = 0
            j += 1
        else:
            i += 1

    return mat3

#quero saber o n-ézimo elemento da fibonnaci de forma FAST
def exponenciacaoMatriz(matriz, n):

    binario = transformaNumeroBinario(n)
    
    #Agora dividimos para conquistar, fazemos o valor de cada mod da exponenciação por partes
    #E MULTIPLICAMOS E ENTÃO SOMENTE FAZEMOS O MOD FINAL

    lista = [matriz for i in binario]

    for i in range(len(binario) -1, -1, -1):
        if i != len(binario) -1:
            lista[i] = multiplicaMatriz(lista[i + 1], lista[i + 1])

    for i in range(len(binario)):
        if binario[i] == "1":
            matriz = multiplicaMatriz(matriz, lista[i])


    return matriz


    """
    (1, 1  ^ n == (Fn + 1, Fn       visto isso iremos fazer uma função
        1, 0)         Fn,   Fn-1)      que calcule matriz ^ n e pegamos então o valor 
    """



#CODE TO CALCULATE A DETERMINANT OF A MATRIZ
def reduzMatriz(matriz, I = 0, J = 0):

    matrizRetornar = [[] for i in range(len(matriz) -1)]

    linhaAtual = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i != I and j != J:
                matrizRetornar[linhaAtual].append(matriz[i][j])
                if len(matrizRetornar[linhaAtual]) == len(matriz[0]) -1:
                    linhaAtual += 1

    return matrizRetornar

def calculaDeterminante(matriz):

    if len(matriz) == 2 and len(matriz[0]) == 2:
        diagonalPrincipal = matriz[0][0] * matriz[1][1]
        diagonalSegunda = matriz[0][1] * matriz[1][0]
        return diagonalPrincipal - diagonalSegunda
    
    if len(matriz) == 3 and len(matriz[0]) == 3:
        diagonalPrincipal = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
        diagonalSegunda = matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][0] * matriz[1][2] * matriz[2][1] + matriz[0][1] * matriz[1][0] * matriz[2][2]
        return diagonalPrincipal - diagonalSegunda

    lista = [i for i in matriz[0]]

    for i in range(len(lista)):
        if i % 2 == 0:
            K = 1
        else:
            K = -1
        
        lista[i] *= K * calculaDeterminante(reduzMatriz(matriz, 0, i))

    return sum(lista)


matriz = [[1,2,3,4],
          [0,1,2,0],
          [1,2,0,0],
          [3,2,2,3]]

print(calculaDeterminante(matriz))
