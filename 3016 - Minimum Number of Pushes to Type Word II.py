from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        common = counts.most_common()
        pushes =  0

        for i, (c, v) in enumerate(common):
            pushes += v * (i // 8 + 1)

        return pushes