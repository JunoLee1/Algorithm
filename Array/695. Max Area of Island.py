class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: #매서드의 인덴테이션은 같아야한다.
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.dx = [0, -1, 0, 1]
        self.dy = [-1, 0, 1, 0]
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.num = 1
        m_island = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and (not self.visited[i][j]):
                    self.bfs(i,j)
                    m_island = max(m_island, self.num)
                    self.num += 1
        return m_island
    
    def bfs(self,i,j):
        Q = []
        Q.append((i,j))
        self.visited[i][j] = True
        while len(Q):
            curr = Q[0]
            Q.pop(0)
            for d in range(4):
                nx = curr[0] + self.dx[d]
                ny = curr[1] + self.dy[d]
                
                if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                    continue
                
                if self.grid[nx][ny] == 0 or self.visited[nx][ny]:
                    continue 
                Q.append((nx, ny))
                self.visited[nx][ny] = True
        return None
            
        