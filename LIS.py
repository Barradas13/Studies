#PROBLEMA DA MAIOR SUBSEQUENCIA CRESCENTE COMUM

def maiorSubCres(i, a, lis):
    if i == 0:
        return 1
    else:
        for j in range(i):
            if a[j] <= a[i]:
                lis[i] = max(lis[i], 1 + maiorSubCres(j, a, lis))
    
    return lis[i]
    

a = [6,2,3,4,1,9,12,4,5]
lis = [1 for i in a]

print(maiorSubCres(len(a) - 1, a, lis))