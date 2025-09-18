class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        n = len(nums)
        l,r = n,0

        for i in range(n):
            if nums[i] != nums2[i]:
                l = min(l, i)
                r = max(r, i)
        
        if l == n: return 0
        return r - l + 1