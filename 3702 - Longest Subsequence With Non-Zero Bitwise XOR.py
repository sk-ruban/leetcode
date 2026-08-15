class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total, zeros, n = 0, 0, len(nums)

        for i in nums:
            total ^= i
            if i == 0: zeros += 1

        if zeros == n: return 0
        if total != 0: return n
        else: return n - 1