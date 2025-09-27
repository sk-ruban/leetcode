class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)

        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x = points[i]
                    y = points[j]
                    z = points[k]

                    curr = 0.5 * abs(x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1]))
                    area = max(area, curr)

        return area