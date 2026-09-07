class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        total = 0

        for c in s:
            c = ord(c) - 97
            new = total + 1 - dp[c]
            total = (new + total) % MOD
            dp[c] += new % MOD

        return total