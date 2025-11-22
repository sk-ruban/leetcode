class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0

        for i in range(n):
            day = i % 7
            week = i // 7

            total += (week + 1 + day)

        return total
