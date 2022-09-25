class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 #to count each 
        if not s:
            return 0
        
        for i in range(1, n + 1):
            
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            if len(s[i-2 : i]) == 2 and "10" <= s[i-2 : i] <= "26":
                dp[i] += dp[i - 2]
        return dp[n]
            