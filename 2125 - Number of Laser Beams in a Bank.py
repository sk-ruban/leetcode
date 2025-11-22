class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = 0

        for row in bank:
            count = row.count('1')
            if count > 0:
                total += (count * prev)
                prev = count

        return total
