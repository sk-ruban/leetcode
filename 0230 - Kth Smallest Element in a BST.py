# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def traverse(node):
            if node is not None:
                nodes.append(node.val)
                traverse(node.right)
                traverse(node.left)

        traverse(root)
        sortedNodes = sorted(nodes)

        return sortedNodes[k-1]