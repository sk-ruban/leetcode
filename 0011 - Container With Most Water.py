class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        i = 0
        j = len(height) - 1

        while i != j:
            line1, line2 = height[i], height[j]
            maxWater = max(maxWater, min(line1, line2) * abs(i - j))
            if line1 < line2:
                i += 1
            else:
                j -= 1

        return maxWater