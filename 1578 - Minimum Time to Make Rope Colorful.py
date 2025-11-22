class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        prev = 0

        for i in range(1, len(colors)):
            if colors[prev] == colors[i]:
                if neededTime[prev] < neededTime[i]:
                    time += neededTime[prev]
                    prev = i
                else:
                    time += neededTime[i]
            else:
                prev = i

        return time