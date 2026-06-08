class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        equal = []

        for n in nums:
            if n < pivot:
                before.append(n)
            if n == pivot:
                equal.append(n)
            if n > pivot:
                after.append(n)

        return before + equal + after