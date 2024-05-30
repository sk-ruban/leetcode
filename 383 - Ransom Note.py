class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteChar = {}
        magazineChar = {}

        for x in ransomNote:
            noteChar[x] = noteChar.get(x, 0) + 1
        for x in magazine:
            magazineChar[x] = magazineChar.get(x, 0) + 1

        for char, count in noteChar.items():
            if magazineChar.get(char, 0) < count:
                return False

        return True