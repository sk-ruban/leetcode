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
    
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')

        for price in prices:
            buy = min(buy, price)
            currentProfit = price - buy
            profit = max(profit, currentProfit)

        return profit