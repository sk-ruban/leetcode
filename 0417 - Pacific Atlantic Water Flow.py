class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean, prevHeight):
            if ((r,c) in ocean or
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight):
                return
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r , c + 1, ocean, heights[r][c])
            dfs(r , c - 1, ocean, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, c, atl, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
