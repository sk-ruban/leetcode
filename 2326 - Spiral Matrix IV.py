# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        t,b,l,r = 0, m, 0, n
        matrix = [[-1] * n for _ in range(m)]

        while head:
            for i in range(l, r):
                if not head: return matrix
                matrix[t][i] = head.val
                head = head.next            
            t += 1
            for i in range(t, b):
                if not head: return matrix
                matrix[i][r - 1] = head.val
                head = head.next
            r -= 1
            for i in range(r - 1, l - 1, -1):
                if not head: return matrix
                matrix[b - 1][i] = head.val
                head = head.next
            b -= 1
            for i in range(b - 1, t - 1, -1):
                if not head: return matrix
                matrix[i][l] = head.val
                head = head.next
            l += 1
            
        return matrix