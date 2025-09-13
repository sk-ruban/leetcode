class Solution:
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        # Write your code here
        nums.sort()
        count = 0

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
                    
        return count