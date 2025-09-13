from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        freq = Counter(s)

        maxV = max((freq[c] for c in freq if c in vowels), default = 0)
        maxC = max((freq[c] for c in freq if c not in vowels), default = 0)

        return maxV + maxC