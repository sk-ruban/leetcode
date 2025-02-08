class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            groups.setdefault("".join(sorted(s)), []).append(s)

        return list(groups.values())
