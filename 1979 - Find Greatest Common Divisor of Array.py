class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s, l = min(nums), max(nums)

        for n in range(s, 0, -1):
            if s % n == 0 and l % n == 0:
                return n