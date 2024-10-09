class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, closed = 0, 0

        for par in s:
            if par == '(':
                opened += 1
            else:
                if opened == 0:
                    closed += 1
                else:
                    opened -= 1

        return opened + closed