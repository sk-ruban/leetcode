class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        profit = []

        for price in prices:
            if price <= current:
                current = price
            else:
                profit.append(price - current)

        return max(profit) if profit else 0