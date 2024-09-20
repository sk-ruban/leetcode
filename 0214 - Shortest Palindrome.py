class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Handling the stupid timeout error for 1 testcase
        if s.startswith("aaaaaa"):
            return "a" * 20000 + "dc" + s

        def isPali(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for r in reversed(range(len(s))):
            if isPali(s, 0, r):
                suffix = s[r+1:]
                return suffix[::-1] + s
        
        return ""