class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid = 0

        for curr in nums:
            if curr != 0:
                left_sum += curr
            else:
                right_sum = total_sum - left_sum
                if left_sum == right_sum:
                    valid += 2
                elif abs(right_sum - left_sum) == 1:
                    valid += 1

        return valid