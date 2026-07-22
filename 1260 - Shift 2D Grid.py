class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        new_grid = [[None for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                pos = (r * cols + c + k) % (rows * cols)
                new_r = pos // cols
                new_c = pos % cols
                new_grid[new_r][new_c] = grid[r][c]

        return new_grid