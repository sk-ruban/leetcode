class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)

        for word in words:
            for char in word:
                if char not in allowed:
                    count -= 1
                    break
            count += 1
        
        return count