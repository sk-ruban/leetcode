class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        for d in range(n // 2 + 1):
            if words[(startIndex + d) % n] == target or words[(startIndex - d) % n] == target:
                return d

        return -1
