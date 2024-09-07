class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare, tortoise = head, head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        return tortoise