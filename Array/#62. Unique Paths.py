class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        if (m == 2 and n== 1) or (m == 1 and n ==2):
            return 1
        res=0
        if m>1:
            res+=self.uniquePaths(m-1,n)
        if n>1:
            res+=self.uniquePaths(m,n-1)
        return res


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # problem def: return the number of possible unique paths that the robot can take to reach the bottom-right corner. the robot only move right or down.
        # f(i,j) = the number of possible unique path from i to j
        # base case :
        # if i == 0 or j == 0:
        #     return 1
        # general case:
        # f(i,j) = f(i,j-1) +f(i-1,j)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        for j in range(m):
            for i in range(n):
                if i == 0 and j == 0 :
                    continue
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
            
            
        
        
    
    

'''
we could use "back tracking" from the recursive way 
each sum of the "return values" tends to turn out value which is the number of path.

'''