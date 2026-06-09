class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l = len(landDuration)
        w = len(waterDuration)
        landEnd, waterEnd = float('inf'), float('inf')

        for i in range(l):
            landEnd = min(landEnd, landStartTime[i] + landDuration[i])

        for j in range(w):
            waterEnd = min(waterEnd, waterStartTime[j] + waterDuration[j])

        best = float('inf')
        for j in range(w):
            best = min(best, max(waterStartTime[j], landEnd) + waterDuration[j])
        for i in range(l):
            best = min(best, max(landStartTime[i], waterEnd) + landDuration[i])

        return best
