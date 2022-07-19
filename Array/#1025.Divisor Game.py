class Solution:
    def divisorGame(self, n: int) -> bool:
        #general : Return true if and only if Alice wins the game, assuming both players play optimally.
        # if n % x == 0 and n == 0, True. n - x = n
        #
        dp = [0]*(n+1)      
        def topdown(i,dp):
            if i == 1:
                return False
            if i == 2:
                return True
            if dp[i] != 0:
                return  dp[i]
            for x in range(i):
               if i % x  ==  0 and not(topdown(i-x)):
                   dp[i] = True 
                   return dp[i]
            else:
                dp[i] = False
                return dp[i]
        return topdown(i,dp)
                .