n, w = [int(x) for x in input().split()]
a = [int(input()) for i in range(n)]

dp = [[0]*(w+1) for i in range(n)]
dp[0][0] = 1

for i in range(n):
    dp[i][a[i]] = 1
    for j in range(w+1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            if j+a[i] <= w:
                dp[i][j+a[i]] = 1
"""    
    for j in dp:
        print(j)
    print("")
"""    
print(dp[n-1][w])
