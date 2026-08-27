class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = total = 0

        for d in str(n):
            if d != '0': 
                x = x * 10 + int(d)
                total += int(d)
        
        return x * total