from collections import Counter

class Solution:

    def maximumLengthSubstring(self, s: str) -> int:
        count = Counter()
        length, l = 0, 0

        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)

        return length
