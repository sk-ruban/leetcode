class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        return [n for n in range(min(seen), max(seen)) if n not in seen]