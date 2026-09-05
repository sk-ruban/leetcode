class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefMax, suffMin = [nums[0]], [nums[-1]]

        for n in nums[1:]:
            if n > prefMax[-1]: prefMax.append(n)
            else: prefMax.append(prefMax[-1])

        for n in nums[-2::-1]:
            if n < suffMin[-1]: suffMin.append(n)
            else: suffMin.append(suffMin[-1])

        for i, (a, b) in enumerate(zip(prefMax, suffMin[::-1])):
            if a - b <= k: return i

        return -1