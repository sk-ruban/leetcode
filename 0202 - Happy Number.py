class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n) 
            sum = 0
        
            for i in str(n):
                sum += int(i) ** 2
            
            n = sum

        return True