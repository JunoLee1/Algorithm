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




        class Solution:
    def numDecodings(self, s: str) -> int:
        #problem def:  return the number of ways to decode from "i - 1" th  to "n" th.
        # i == 0: return 1
        # if f(i) == 0: return 0
        n = len(s)
        dp = [0] *(n + 1)
    def topdown(self, i, dp):
        if i == 0:
            return 1

        if dp[i] != 0:
            return dp[i]

        if 1 <= self.topdown(i - 1, dp) <= 10 and s[i-1] != "0":
            dp[i] += self.topdown(i - 1, dp)

        if 10 <= self.topdown(i - 2, dp) <= 26:
            dp[i] += self.topdown(i - 2, dp)
                
        return dp[n]
    
    
        
    


    
    
   
            