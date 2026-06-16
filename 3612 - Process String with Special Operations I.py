class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for c in s:
            match c:
                case "*":
                    if len(result) >= 1:
                        result.pop()
                case "#":
                    result.extend(result)
                case "%":
                    result.reverse()
                case c if c.islower():
                    result.append(c)

        return "".join(result)