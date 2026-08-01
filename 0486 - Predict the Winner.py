class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0: return True

        @cache
        def diff(l, r):
            if l == r: return nums[l]
            return max(nums[l] - diff(l+1, r), nums[r] - diff(l, r-1))

        return diff(0, n - 1) >= 0
