class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1 or n == 2:
            return True
        if n % 2 == 1:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)