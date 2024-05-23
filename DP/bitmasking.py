"""
J1,J2,J3 ... Jn Jobs
P1,P2,p3.... Pn People

assign the people to exacly one job each
finds the minumus cost

the ideia here is to use a mask to represent the people
that can be assigned; furthermore we will use a dp table
representing [ith job][mask] that will receive the minimum
for all active j's in that especific job

"""

def solve(job, mask, dp, cost_matriz, N):
    #we have already assigned all jobs
    if job == N:
        return 0

    if dp[job][mask] != -1:
        return dp[job][mask]
    
    
    ans = float("inf")

    for i in range(N):
        #this means that the person is available
        if mask & (1 << i):
            ans = min(ans, cost_matriz[i][job] + solve(job + 1, mask^(1<<i), dp, cost_matriz, N))
    
    dp[job][mask] = ans

    return ans
    


cost_matriz = [[9,2,7,8],
               [6,4,3,7],
               [5,8,1,8],
               [7,6,9,4]]

N = len(cost_matriz)

#the ith represents the job the jth represents the person
#the ith jth represents the cost person j to do job i

#our dp will have [n][(1<<n) - 1] to represents all mask and all jobs
dp = [[-1 for j in range((1<<N))] for i in range(N)]

print(solve(0, (1<<N) - 1, dp, cost_matriz, N))
print((1<<N) - 1)
print(dp)