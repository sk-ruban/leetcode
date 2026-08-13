from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        l, longest = 0, 0

        for r, n in enumerate(nums):
            count[n] += 1
            while count[n] > k:
                count[nums[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest