class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checker(string: str) -> list:
            res = []
            for char in string:
                if char == '#' and res:
                    res.pop(-1)
                elif char == "#":
                    continue
                else:
                    res.append(char)
            return res

        return checker(s) == checker(t)