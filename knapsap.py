def knapsap(valores, pesos, memo, i, w):
    
    if memo[i][w] != -1:
        return memo[i][w]
    else:
        #calcula memo
        if i == 0 or w == 0:
            memo[i][w] = 0
            return 0
        else:
            if w - pesos[i] >= 0:
                memo[i][w] = max(knapsap(valores, pesos, memo, i - 1, w), valores[i] + knapsap(valores, pesos, memo, i-1, w - pesos[i]))
            else:
                memo[i][w] = 0
            return memo[i][w]

pesos = {1:2, 2:3, 3:2, 4:4, 5:6}
valores = {1:6, 2:14, 3:7, 4:18, 5:24}

b = 8

memo = []

for i in range(len(pesos) + 1):
    memo.append([])
    for j in range(b + 1):
        memo[i].append(-1)

print(knapsap(valores, pesos, memo, 5, b))