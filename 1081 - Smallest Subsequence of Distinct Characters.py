from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count = Counter(s)

        for c in s:
            count[c] -= 1

            if c in stack:
                continue

            while stack and count[stack[-1]] > 0 and c < stack[-1]:
                stack.pop()

            stack.append(c)

        return "".join(stack)