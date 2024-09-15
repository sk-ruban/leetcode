class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, combi):
            if len(combi) == k:
                res.append(combi.copy())
                return

            for i in range(start, n + 1):
                combi.append(i)
                backtrack(i+1, combi)
                combi.pop()
        
        backtrack(1, [])
        return res
