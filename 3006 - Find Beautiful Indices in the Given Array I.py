class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        slen = len(s)
        alen = len(a)
        blen = len(b)
        beautiful = []

        idxI = [i for i in range(0, slen - alen + 1) if s[i : i + alen] == a]
        idxJ = [i for i in range(0, slen - blen + 1) if s[i : i + blen] == b]

        j = 0

        for i in idxI:
            while j < len(idxJ) and idxJ[j] < i - k:
                j += 1
            if j < len(idxJ) and idxJ[j] <= i + k:
                beautiful.append(i)

        return beautiful