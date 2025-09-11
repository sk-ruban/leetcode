class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(c):
            vowels = {'a','e','i','o','u'}
            return c.lower() in vowels
        
        vowels = []

        for c in s:
            if isVowel(c):
                vowels.append(c)
        
        vowels.sort()
        s2 = ""
        vidx = 0

        for i in range(len(s)):
            if isVowel(s[i]):
                s2 += vowels[vidx]
                vidx += 1
            else:
                s2 += s[i]

        return s2