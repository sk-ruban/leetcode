class Solution:
    def longestPalindrome(self, s: str) -> int:
        char = {}
        length = 0
        hasOdd = False

        for i in s:
            char[i] = char.get(i, 0) + 1

        for num in char.values():
            if num % 2 == 0:
                length += num
            else:
                length += num - 1
                hasOdd = True

        return length + 1 if hasOdd else length