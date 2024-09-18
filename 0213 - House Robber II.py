class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        curr, prev = 0, 0
        for n in nums:
            curr, prev = max(curr, prev + n), curr
        return curr