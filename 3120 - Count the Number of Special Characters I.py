class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        upper = set()
        lower = set()

        for c in word:
            if c.islower():
                lower.add(c)
            if c.isupper():
                upper.add(c)

        for c in upper:
            if c.lower() in lower:
                special += 1

        return special