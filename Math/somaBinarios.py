n1 = "101"
n2 = "110"
n3 = ""

i = len(n2) -1
somAcumulada = 0

while i >= 0:
    soma = int(n1[i]) + int(n2[i]) + somAcumulada
    if soma > 1:
        n3 = "0" + n3
        somAcumulada = 1
    else:
        n3 = str(soma) + n3
        somAcumulada = 0
    i -= 1
    
n3 = str(somAcumulada) + n3

print(n3)