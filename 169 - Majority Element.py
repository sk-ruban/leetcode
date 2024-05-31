class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0

        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        return candidate