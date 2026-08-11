class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total, setnums = nums[0], set(nums)

        for a, b in pairwise(nums):
            if b == a + 1:
                total += b
            else:
                break

        while total in setnums:
            total += 1

        return total
