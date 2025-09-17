class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(c, i):
            count = 0
            while i >= 0:
                if c[i] == '#':
                    count += 1
                elif count > 0:
                    count -= 1
                else:
                    return i, c[i]
                i -= 1
            return -1, None

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i, c1 = backspace(s, i)
            j, c2 = backspace(t, j)

            if c1 != c2:
                return False

            if i >= 0: i -= 1
            if j >= 0: j -= 1

        return True
