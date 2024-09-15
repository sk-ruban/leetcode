class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"

        res = 0
        mask = 0
        maskIndex = {0:-1}

        for i,c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in maskIndex:
                length = i - maskIndex[mask]
                res = max(length, res)
            else:
                maskIndex[mask] = i

        return res