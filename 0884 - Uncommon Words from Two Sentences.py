class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split() + s2.split())
        return [w for w,i in count.items() if i == 1]