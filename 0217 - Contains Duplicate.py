class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)