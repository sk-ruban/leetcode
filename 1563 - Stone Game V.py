class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        accum = [0] + list(accumulate(stoneValue))

        @cache
        def dp(l, r):
            if l == r: return 0
            best = 0
            for i in range(l, r):
                L = accum[i+1] - accum[l]
                R = accum[r+1] - accum[i+1]
                if L < R:
                    if best >= 2*L: continue
                    best = max(best, L + dp(l, i))
                elif L > R:
                    if best >= 2*R: break
                    best = max(best, R + dp(i+1, r))
                else: best = max(best, L + dp(l, i), R + dp(i+1, r))

            return best

        return dp(0, len(stoneValue)-1)
