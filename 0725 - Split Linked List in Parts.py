# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        base_len, remainder = length // k, length % k
        curr = head
        res = []

        for _ in range(k):
            res.append(curr)
            for _ in range(base_len + (0 if remainder else -1)):
                if not curr: break
                curr = curr.next
            remainder -= 1 if remainder else 0
            if curr:
                curr.next, curr = None, curr.next

        return res