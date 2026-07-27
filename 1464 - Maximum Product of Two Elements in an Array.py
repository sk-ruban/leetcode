class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        val = 0

        for i in range(N):
            for j in range(i+1, N):
                val = max(val, (nums[i]-1)*(nums[j]-1))

        return val