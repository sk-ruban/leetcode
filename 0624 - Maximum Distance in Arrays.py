class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curr_min, curr_max = arrays[0][0], arrays[0][-1]
        diff = 0

        for i in range(1, len(arrays)):
            diff = max(
                diff,
                curr_max - arrays[i][0],
                arrays[i][-1] - curr_min
            )
            curr_min = min(curr_min, arrays[i][0])
            curr_max = max(curr_max, arrays[i][-1])
        
        return diff