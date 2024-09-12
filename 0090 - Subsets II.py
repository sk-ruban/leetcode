class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        for i in nums:
            tmp = []
            for r in res:
                if r + [i] not in res:
                    tmp.append(r + [i])
                tmp.append(r)
            res = tmp

        return res