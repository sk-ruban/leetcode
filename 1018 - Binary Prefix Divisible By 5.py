class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = ""
        answer = []

        for n in nums:
            curr += str(n)
            answer.append(int(curr, 2) % 5 == 0)

        return answer
