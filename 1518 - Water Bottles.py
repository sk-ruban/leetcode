class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty = 0

        while numBottles > 0:
            count += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return count
