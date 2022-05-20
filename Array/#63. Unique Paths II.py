class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def path (i,j):
            if obstacleGrid[i][j] == 1:
                return 0
            elif(i,j) in self.grid:
                return self.grid[(i,j)]
            else :
                right = down =0
                if i < len(obstacleGrid)-1 :
                    down = path(i+1,j)
                if j < len(obstacleGrid[0])-1:
                    right = path(i,j+1)
            temp = down + right
            self.grid[(i,j)] = temp
            return temp
        self.grid = collections.defaultdict(int)
        self.grid[(len(obstacleGrid) - 1, len(obstacleGrid[0])-1)] = 1
        return path(0,0)
                
            