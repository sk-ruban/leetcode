class Solution:
    def sumGame(self, num: str) -> bool:
        h = len(num) // 2
        l, r = num[:h], num[h:]
        f = lambda s: sum(map(int, s.replace('?', '0'))) + 4.5 * s.count('?')

        return f(l) != f(r)