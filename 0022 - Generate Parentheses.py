class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(op, cl, s):
            if len(s) == 2 * n:
                res.append(s)
                return
            if op < n: dfs(op + 1, cl, s + '(')
            if cl < op: dfs(op, cl + 1, s + ')')

        dfs(0, 0, '')
        return res
