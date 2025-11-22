class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for l in left:
                if right[l] > 0:
                    res.add((m,l))
            left.add(m)

        return len(res)
