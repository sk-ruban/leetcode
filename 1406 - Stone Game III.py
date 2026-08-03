class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def take(i):
            if i == n: return 0
            a = b = c = float('-inf')
            
            if i < n: a = stoneValue[i] - take(i+1)
            if i+1 < n: b = stoneValue[i] + stoneValue[i+1] - take(i+2)
            if i+2 < n: c = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - take(i+3)

            return max(a, b, c)

        match take(0):
            case x if x > 0: return "Alice"
            case x if x < 0: return "Bob"
            case _: return "Tie"