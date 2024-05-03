#encontrar o subarray com máximo valor numérico

def kadane(arr):
    soma_atual = arr[0]
    max_soma = arr[0]
    
    for i in arr[1:]:
        soma_atual = max(soma_atual + i, i)
        max_soma = max(soma_atual, max_soma)

    return max_soma

lista = [5,-10,1,-2,3,4,7]

print(kadane(lista))
