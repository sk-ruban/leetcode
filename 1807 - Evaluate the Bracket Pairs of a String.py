class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = dict(knowledge)
        i, n = 0, len(s)
        res = []

        while i < n:
            if s[i] == "(":
                j = s.index(")", i)
                res.append(mapping.get(s[i + 1:j], "?"))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        
        return "".join(res)
