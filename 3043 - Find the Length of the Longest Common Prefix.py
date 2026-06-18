class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1set = set()
        arr2set = set()

        for n in arr1:
            nstr = str(n)
            for i in range(1, len(nstr)+1):
                arr1set.add(nstr[:i])

        for n in arr2:
            nstr = str(n)
            for i in range(1, len(nstr)+1):
                arr2set.add(nstr[:i])

        common = arr1set.intersection(arr2set)

        return len(max(common, key=len)) if len(common) > 0 else 0