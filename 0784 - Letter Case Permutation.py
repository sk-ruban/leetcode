class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]

        for c in s:
            tmp = []
            if c.isalpha():
                for i in output:
                    tmp.append(i + c.lower())
                    tmp.append(i + c.upper())
            else:
                for i in output:
                    tmp.append(i + c)
            output = tmp

        return output