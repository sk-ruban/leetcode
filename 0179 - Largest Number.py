class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1   # Don't switch
            else:
                return 1    # Switch
        
        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))