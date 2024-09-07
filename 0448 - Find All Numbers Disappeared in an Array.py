class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numRange = set(range(1, len(nums) + 1))
        return list(numRange - set(nums))