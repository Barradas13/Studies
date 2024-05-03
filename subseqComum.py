A = "nxsxexixaa"
B = "nseiaa"

def LCS(A, B, iA=0, iB=0):
    if len(A) == 0 or len(B) == 0:
        return 0
    if len(A) <= iA or len(B) <= iB:
        return 0
    #a primeira é igual ent 1+LCS(A`, B`)
    elif A[iA] == B[iB]:
        return 1+LCS(A, B, iA+1, iB+1)
    else:
        return max(LCS(A, B, iA + 1, iB), LCS(A, B, iA, iB + 1))

def substring(A, B):
    #tabela de respostas, diz a semelhanca entre a[i] b[j] 
    tabAns = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    resposta = 0

    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                tabAns[i][j] = tabAns[i-1][j-1] + 1
                resposta = max(tabAns[i][j], resposta)

    return resposta

print(substring(A, B))