class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        res = []

        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(original[i * 2 + j])

        return res
    
    def construct2DArray2(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return [original[n * i : n * (i + 1)] for i in range(m)]