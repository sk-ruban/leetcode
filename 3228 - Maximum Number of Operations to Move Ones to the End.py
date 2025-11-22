class Solution:
    def maxOperations(self, s: str) -> int:
        res, one_count = 0, 0

        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
            elif i > 0 and s[i-1] == '1':
                res += one_count

        return res