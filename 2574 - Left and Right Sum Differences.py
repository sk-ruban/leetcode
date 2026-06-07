class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        start, end = 0, sum(nums)
        res = []

        for n in nums:
            res.append(abs(start - end + n))
            start += n
            end -= n

        return res