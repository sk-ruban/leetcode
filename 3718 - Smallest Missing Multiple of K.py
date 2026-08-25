class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mult, arr = k, set(nums)

        while mult in arr:
            mult += k

        return mult