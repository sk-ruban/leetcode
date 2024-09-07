class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1
        for x in t:
            count[x] = count.get(x, 0) - 1

        for val in count.values():
            if val != 0:
                return False

        return True