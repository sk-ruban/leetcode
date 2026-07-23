class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        size, i = len(nums), 2

        if size == 1: return 1
        if size == 2: return 2

        while i <= size:
            i *= 2

        return i