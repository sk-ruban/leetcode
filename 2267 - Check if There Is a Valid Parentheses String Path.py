class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        r, c = len(grid), len(grid[0])

        if (r + c) % 2 == 0 or grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        @cache
        def dfs(x, y, a):
            a += 1 if grid[x][y] == '(' else -1

            if a < 0 or a > (r + c - 1) - (x + y):
                return False

            if x == r - 1 and y == c - 1:
                return a == 0

            return (x < r - 1 and dfs(x+1, y, a)) or (y < c - 1 and dfs(x, y+1, a))

        return dfs(0, 0, 0)
