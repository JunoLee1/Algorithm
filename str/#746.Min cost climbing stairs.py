def minCostClimbingStairs(self, cost: List[int]) -> int:
        #general: Return the minimum cost to reach the top of the floor. Once you pay the cost, you can either climb one or two steps.
        #baseCase: if n < 0, return 0
        #relation :cost[i] + min(cost[i-1],cost[i-2])
        dp = [[-1]*(len(cost)+1)]
        def dfs(self,idx):
            if idx < 0: # 만약 인덱스 번호가 0보다 작으면
                return 0
            dp[idx] = cost[idx] + min(dp[idx-1],dp[idx-2]) 
        return min(dp[idx-1],dp[idx-2])