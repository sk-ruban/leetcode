class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for x in range(1, 1 + (i // 2)):
                if i % x == 0:
                    dp[i] = min(dp[i], dp[x] + i // x)

        return dp[n]