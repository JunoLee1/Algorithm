class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #general: Return the minimum cost to reach the top of the floor.
        #min(minCost(n-1),minCost(n-2))
        #base case : if idx >= 0 return 0
        m = {}
        def dfs(idx,cost):
            nonlocal m
            
            if idx >= len(cost):
                return 0
            
            if idx in m :
                return m[idx]
            
            res = cost[idx] + min(dfs(idx+1,cost), dfs(idx+2,cost))
            m[idx] = res
            return res
        return min(dfs(0,cost),dfs(1,cost))