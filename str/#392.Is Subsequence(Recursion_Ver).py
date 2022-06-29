def isSubsequence(self, s, t):
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False
    if s[0] == t[0]:
        return self.isSubsequence(s[1:],t[1:])
    else:
        return self.isSubsequence(s,t[1:])

def isSubsequence(self, s, t):
    m = len(s)
    n = len(t)

    if n == 0: #len(s)가 0이면 true
        return True
        
    if m == 0:
        return False
        
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
    for i in range(1,m+1):
        for j in range(1,n+1):
                
            if t[i-1] == s[j-1]: #t와 s의 뽑은 요소가 같다면
                dp[i][j] = dp[i-1][j-1] + 1 #LCS(i-1,j-1)에다가 길이 +1
                
            else: 
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            if dp[i][j] == len(s):
                return True
    return False
        