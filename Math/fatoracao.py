def crivoErastotenes(n):
    tabelaMultiplos = [True for i in range(n)]

    for i in range(2, len(tabelaMultiplos) + 1):
        if tabelaMultiplos[i - 1]:
            j = i
        
            while j + i <= n:
                j += i
                tabelaMultiplos[j - 1] = False
                
        
    resposta = []

    for i in range(1, len(tabelaMultiplos)):
        if tabelaMultiplos[i]:
            resposta.append(i + 1)

    return resposta

def divPtentativa(n):
    i = 2

    divisores = []

    while i * i < n:
        if n % i == 0:
            divisores.append(i)
            divisores.append(int(n/i))

        i += 1
    
    return divisores

def fatoracaoComDivPtentativa(n):
    i = 2

    divisores = []

    while i * i <= n:

        if n % i == 0:
            divisores.append(i)
            n = int(n/i)
        else:
            i += 1
    
    divisores.append(n)

    return divisores

def fatoracaoComCrivo(n):
    divisores = []

    primos = crivoErastotenes(n)
    i = primos[0]

    for i in primos:
        while n % i == 0 and i != n:
            divisores.append(i)
            n = int(n/i)

    divisores.append(n)

    return divisores

#print(fatoracaoComCrivo(62312313)) // demoradasso pois primeiro calculo todos os primos....
print(fatoracaoComDivPtentativa(62312313))
