class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def convertTime(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        res = 24 * 60 - convertTime(timePoints[-1]) + convertTime(timePoints[0])

        for i in range(len(timePoints) - 1):
            curr = convertTime(timePoints[i + 1])
            prev = convertTime(timePoints[i])
            diff = curr - prev
            res = min(diff, res)
            if res == 0:
                break

        return res