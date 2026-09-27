class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = res = []
        pairs = [-1] * n

        for i in range(n):
            if s[i] == '(': 
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i

        i, dir = 0, 1
        while 0 <= i < n:
            if s[i] in '()': 
                i = pairs[i]
                dir = -dir
            else:
                res.append(s[i])
            i += dir

        return "".join(res)