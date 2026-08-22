class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p = 0, 1
        
        for c in str(n):
            s += int(c)
            p *= int(c)
        
        return n % (s + p) == 0