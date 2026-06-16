class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        upper = {}
        lower = {}

        for i in range(len(word)):
            c = word[i]

            if c.islower():
                lower[c] = i
            if c.isupper() and c not in upper:
                upper[c] = i

        for c in lower:
            if c.upper() in upper and lower[c] < upper[c.upper()]:
                special += 1

        return special