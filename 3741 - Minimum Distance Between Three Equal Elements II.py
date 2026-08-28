from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos, best = defaultdict(list), float("inf")
        
        for i, v in enumerate(nums):
            pos[v].append(i)

        for p in pos.values():
            if len(p) < 3: continue
            for a in range(len(p) - 2):
                best = min(best, 2 * (p[a+2] - p[a]))

        return -1 if best == float("inf") else best
