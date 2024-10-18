class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        maxDigit = "0"
        max_i = -1
        swap_i = swap_j = -1

        for i in reversed(range(len(num))):
            if num[i] > maxDigit:
                maxDigit = num[i]
                max_i  = i

            if num[i] < maxDigit:
                swap_i, swap_j = i, max_i

        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int("".join(num))
