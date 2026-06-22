from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textcount = Counter(text)
        need = Counter("balloon")

        inst = float("inf")
        for c in need:
            if c in textcount:
                inst = min(inst, textcount[c] // need[c])
            else:
                return 0

        return inst