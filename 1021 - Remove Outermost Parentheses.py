class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        base = 0
        res = ""

        for c in s:
            if c == '(':
                if base > 0: res += c
                base += 1
            else:
                base -= 1
                if base > 0: res += c

        return res
