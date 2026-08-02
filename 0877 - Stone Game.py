class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n % 2 == 0: return True

        @cache
        def take(l, r):
            if l == r: return piles[l]
            return max(piles[l] - take(l+1, r), piles[r] - take(l, r-1))

        return take(0, n-1)