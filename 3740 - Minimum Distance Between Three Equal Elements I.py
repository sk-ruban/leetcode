class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        best = float('inf')

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        best = min(best, abs(i - j) + abs(j - k) + abs(k - i))

        return -1 if best == float('inf') else best