from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        self.dfs(image, sr, sc, color, start)
        return image

    def dfs(self, image, sr, sc, color, start):
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] != start or image[sr][sc] == color:
            return
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, start)
        self.dfs(image, sr-1, sc, color, start)
        self.dfs(image, sr, sc+1, color, start)
        self.dfs(image, sr, sc-1, color, start)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        old_color = image[sr][sc]

        if old_color == color:
            return image

        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        def bfs():
            visited = {(sr, sc)}
            queue = deque([(sr, sc)])

            while queue:
                pr, pc = queue.popleft()
                image[pr][pc] = color

                for nr, nc in neighbours(pr, pc):
                    if (nr, nc) not in visited and image[nr][nc] == old_color:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            return image

        return bfs()
