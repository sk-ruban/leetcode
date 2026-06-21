class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxVal = max(costs)
        count = [0] * (maxVal + 1)
        res = 0

        for c in costs:
            count[c] += 1

        for price in range(1, maxVal + 1):
            if count[price] == 0:
                continue
            if coins < price:
                break
            buyable = min(count[price], coins // price)
            res += buyable
            coins -= buyable * price

        return res