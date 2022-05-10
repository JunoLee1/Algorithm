def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n]
print(tribonacci(3))