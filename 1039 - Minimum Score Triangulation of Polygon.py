class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            if j - i < 2: return 0
            score = float('inf')

            for k in range(i+1, j):
                curr = values[i] * values[j] * values[k]
                score = min(score, curr + dp(i,k) + dp(k,j))

            return score

        return dp(0, len(values) - 1)