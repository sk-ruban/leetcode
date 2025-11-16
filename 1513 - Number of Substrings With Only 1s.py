class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        count = 0
        consecutive = 0

        for c in s:
            if c == '1':
                consecutive += 1
                count += consecutive
            else:
                consecutive = 0
        
        return count % mod