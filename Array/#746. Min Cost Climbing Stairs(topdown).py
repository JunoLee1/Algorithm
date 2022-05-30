class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #general: Return the minimum cost to reach from 0 to the "i"th stair case given cost array
        #base case: if  i < 0, return 0
        #general case: dp[i] = cost[i] + min(dp[i-1], dp[i-2]) 
        def topdown(i, cost):
            if i < 0:
                return 0
            
            return cost[i] + min(topdown(i-1, cost), topdown(i-2, cost))
        dp = [-1]*(n+1)
        n = len(cost)
        return min(dp(n-1, cost), dp(n-2, cost))

    
     