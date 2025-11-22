class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def inc(idx):
            for i in range(idx, idx + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for i in range(0, len(nums) - 2*k + 1):
            if inc(i) and inc(i + k):
                return True

        return False