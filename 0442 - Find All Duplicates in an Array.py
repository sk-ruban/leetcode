class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                res.append(i)
            nums[i - 1] *= -1

        return res