from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        counts = Counter(nums)
        expected = {v:1 for v in range(1, n)}
        expected[n] = 2
        
        return expected == counts