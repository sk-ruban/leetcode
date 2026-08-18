from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n: return max(nums)
        
        count = Counter(nums)
        c = set(nums) if k == 1 else {nums[0], nums[-1]}

        return max([x for x in c if count[x] == 1], default = -1)