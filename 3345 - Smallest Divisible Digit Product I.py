from functools import reduce

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while reduce(lambda x, y: x * y, [int(c) for c in str(n)], 1) % t:
            n += 1

        return n