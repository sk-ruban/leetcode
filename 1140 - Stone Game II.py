class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = piles[i] + suffix[i+1]

        @cache
        def dp(i, m):
            if i == n: return 0
            if 2 * m >= n - i: return suffix[i]

            total = 0
            for x in range(1, 2*m + 1):
                total = max(total, suffix[i] - dp(i + x, max(m, x)))

            return total
        
        return dp(0, 1)