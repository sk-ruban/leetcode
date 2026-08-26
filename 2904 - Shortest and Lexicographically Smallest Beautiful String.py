class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, c in enumerate(s) if c == '1']
        if len(ones) < k: return ""

        best = None
        for i in range(len(ones) - k + 1):
            sub = s[ones[i] : ones[i + k - 1] + 1]
            if best is None or (len(sub), sub) < (len(best), best):
                best = sub

        return best