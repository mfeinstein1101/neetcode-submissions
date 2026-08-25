class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(nodes):
            q = deque(nodes)
            visited = set()
            level = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                        continue
                    grid[r][c] = level
                    visited.add((r, c))
                    q.append((r+1, c))
                    q.append((r-1, c))
                    q.append((r, c+1))
                    q.append((r, c-1))
                level += 1

        
        nodes = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    nodes.append((i, j))
        
        bfs(nodes)
                