class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for x, y in zip(nums, nums[1:]):
                nxt.append((x+ y) % 10)
            nums = nxt

        return nums[0]
