class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (nextR < 0 or nextC < 0 or
                    nextR > N-1 or nextC > N-1 or
                    (nextR, nextC) in visit):
                    continue    
                visit.add((nextR, nextC))
                heapq.heappush(minHeap, [max(t, grid[nextR][nextC]), nextR, nextC])