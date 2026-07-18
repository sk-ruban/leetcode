class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        window = "123456789"
        l, h = len(str(low)), len(str(high))
        seq = []

        for k in range(l, h+1):
            for i in range(0, len(window) + 1 - k):
                val = int(window[i:i+k])
                if low <= val <= high:
                    seq.append(val)

        return seq