class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)

        @cache
        def dp(idx):
            if idx >= N: return 0
            return energy[idx] + dp(idx + k)

        best = float('-inf')
        for i in range(N):
            best = max(best, dp(i))

        return best