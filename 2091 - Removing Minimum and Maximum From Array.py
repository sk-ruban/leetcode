class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        high, low = nums.index(max(nums)), nums.index(min(nums))
        a, b = min(high, low), max(high, low)

        front = b + 1
        back = n - a
        frontback = 1 + a + n - b

        return min(front, back, frontback)