class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0

        for n in range(num1, num2 + 1):
            num = str(n)
            for i in range(1, len(num) - 1):
                if (num[i] > num[i-1] and num[i] > num[i+1]) or (num[i] < num[i-1] and num[i] < num[i+1]):
                    waviness += 1

        return waviness
