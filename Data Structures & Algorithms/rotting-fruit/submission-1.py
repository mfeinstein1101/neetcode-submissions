class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        n, m = len(grid), len(grid[0])

        fresh = 0
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        dirs = [[0, 1], [0,-1], [1,0], [-1,0]]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in dirs:
                    r, c = i + di, j + dj

                    if r in range(n) and c in range(m) and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh -= 1
            res += 1
        
        return res if fresh == 0 else -1
