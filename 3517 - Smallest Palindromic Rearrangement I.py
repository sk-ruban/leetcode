from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        lexi = sorted(counts)
        output = ""
        middle = ""

        for c in lexi:
            if counts[c] % 2 != 0:
                middle = c
            output += c * (counts[c] // 2)

        return output + middle + output[::-1]