class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fullRange = set(range(0, len(nums) + 1))
        return (fullRange - set(nums)).pop()
    
    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        actualSum = sum(nums)
        expectedSum = (n * (n + 1)) // 2
        return expectedSum - actualSum