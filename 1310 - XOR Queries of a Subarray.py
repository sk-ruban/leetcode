class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        res = []

        for i in arr:
            prefix.append(prefix[-1] ^ i)

        for left, right in queries:
            res.append(prefix[left] ^ prefix[right + 1])

        return res