class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True

        return False