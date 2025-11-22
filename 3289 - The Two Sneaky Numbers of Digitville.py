from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        sneaky = counts.most_common(2)
        return [k for k,v in sneaky]