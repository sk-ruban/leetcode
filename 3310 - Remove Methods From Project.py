class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        mapping = {i:[] for i in range(n)}
        for a, b in invocations:
            mapping[a].append(b)

        queue = [k]
        visited = set(queue)

        while queue:
            sus = queue.pop()
            for nxt in mapping[sus]:
                if nxt not in visited:
                    visited.add(nxt) 
                    queue.append(nxt)
        
        for a, b in invocations:
            if a not in visited and b in visited:
                return [i for i in range(n)]

        return [i for i in range(n) if i not in visited]