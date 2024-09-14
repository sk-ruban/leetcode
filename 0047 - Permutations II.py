class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    perm.append(n)

                    dfs()
                    count[n] += 1
                    perm.pop()

        dfs()
        return res