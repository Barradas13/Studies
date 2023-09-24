palavra = input()

subcadeias = []

for j in range(len(palavra)):
        corrente = ''
        for k in range(j,len(palavra)):
            corrente += palavra[k]
            subcadeias.append(corrente)
    
print(subcadeias)