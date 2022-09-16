class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: #매서드의 인덴테이션은 같아야한다.
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.dx = [0, -1, 0, 1]
        self.dy = [-1, 0, 1, 0]
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        m_island = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and (not self.visited[i][j]):
                    m_island = max(m_island, self.bfs(i,j))
        return m_island
    
    def bfs(self,i,j):
        Q = []
        Q.append((i,j))
        self.visited[i][j] = True
        area = 1 #너비는 1 
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
                area += 1 # 너비에 1씩 더해준다 
        return area 
        _________________________________________*100
        class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: #매서드의 인덴테이션은 같아야한다.
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
        max_area = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and (not self.visited[i][j]):
                    max_area = max(max_area, self.dfs(i, j))
        return max_area 
    
    def dfs(self, i, j):
        area = 1 #첫 땅
        
        if i < 0 or j < 0 or i >= self.m or j >= self.n:        
            return None
        
        if self.grid[i][j] == 0 or self.visited[i][j]:
            return None
        
        self.visited[i][j] = True
        
        for d in range(4):
            nx = i + self.dx[d]
            ny = j + self.dy[d]
      
            area += 1
            self.dfs(nx,ny)
        return area
       
        
        
        



            
        