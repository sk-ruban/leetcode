class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        bit = max(nums)
        res = 0
        stored = 0

        for i in nums:
            if i == bit:
                res += 1
            else:
                res = 0
            stored = max(stored, res)

        return stored