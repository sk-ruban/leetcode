class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = {}
        N = len(nums2)

        for i in range(N):
            curr = nums2[i]
            stack[curr] = -1

            for j in range(i+1, N):
                new = nums2[j]
                if new > curr:
                    stack[curr] = new
                    break

        return [stack[n] for n in nums1]
