class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f = Counter(digits)
        total = 0

        for n in range(100, 1000, 2):
            h, r = divmod(n, 100)
            t, o = divmod(r, 10)
            total += f[h] > 0 and f[t] > (t == h) and f[o] > (o == h) + (o == t)
        
        return total