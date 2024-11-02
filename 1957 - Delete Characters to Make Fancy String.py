class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy = s[0:2]

        for i in range(2, len(s), 1):
            if not (fancy[-1] == fancy[-2] == s[i]):
                fancy += s[i]

        return fancy