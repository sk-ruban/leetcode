class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        squared = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squared.append(nums[left] ** 2)
                left += 1
            else:
                squared.append(nums[right] ** 2)
                right -= 1
            
        return squared[::-1]