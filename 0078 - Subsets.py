class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            tmp = []
            for r in res:
                tmp.append(r + [n])
                tmp.append(r)
            res = tmp

        return res