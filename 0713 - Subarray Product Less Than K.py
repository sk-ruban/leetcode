class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        product = 1
        l = 0

        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            count += (r - l + 1)

        return count