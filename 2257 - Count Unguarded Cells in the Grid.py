class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 2

        for r, c in walls:
            grid[r][c] = 3

        def check(r, c):
            for row in range(r-1, -1, -1):
                if grid[row][c] in [2, 3]:
                    break
                grid[row][c] = 1
            for row in range(r+1, m):
                if grid[row][c] in [2, 3]:
                    break
                grid[row][c] = 1
            for col in range(c-1, -1, -1):
                if grid[r][col] in [2, 3]:
                    break
                grid[r][col] = 1
            for col in range(c+1, n):
                if grid[r][col] in [2, 3]:
                    break
                grid[r][col] = 1

        for r, c in guards:
            check(r,c)

        return sum(row.count(0) for row in grid)