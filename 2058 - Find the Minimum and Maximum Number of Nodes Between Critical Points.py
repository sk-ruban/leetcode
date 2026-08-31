# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = last = -1
        mindist = float("inf")
        prev, curr, i = head, head.next, 1

        while curr and curr.next:
            if (curr.next.val - curr.val) * (prev.val - curr.val) > 0:
                if first < 0:
                    first = i
                else:
                    mindist = min(mindist, i - last)
                last = i
            
            prev, curr, i = curr, curr.next, i+1

        return [-1, -1] if first == last else [mindist, last - first]