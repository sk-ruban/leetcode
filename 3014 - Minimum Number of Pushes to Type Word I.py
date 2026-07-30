class Solution:
    def minimumPushes(self, word: str) -> int:
        k, r = divmod(len(word), 8)
        count = 0

        while k >= 0:
            count += (k + 1) * r
            k -= 1
            r = 8

        return count