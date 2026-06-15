from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1_000_000_007
        nodes = len(edges) + 1
        graph = [[] for _ in range(nodes + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist = [-1] * (nodes + 1)
        dist[1] = 0
        queue = deque([1])
        depth = 0

        while queue:
            node = queue.popleft()
            for n in graph[node]:
                if dist[n] == -1:
                    dist[n] = dist[node] + 1
                    depth = max(depth, dist[n])
                    queue.append(n)

        return pow(2, depth - 1, mod)