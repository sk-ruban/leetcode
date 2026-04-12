from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                val = grid[row][col]

                for row, col in neigbours(grid, row, col, val):
                    if (row, col) not in visited:
                        visited.add((row,  col))
                        queue.append((row, col))

        def neigbours(grid, r, c, val):
            indices = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            return [(row, col) for row, col in indices if isValid(grid,row, col) and grid[row][col] == val]

        def isValid(grid, r, c):
            return r >= 0 and c >= 0 and r < rows and c < cols

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)

        return islands
