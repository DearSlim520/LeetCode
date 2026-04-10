# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.ind = k
        def bst(node):
            if not node:
                return
            
            bst(node.left)
            self.ind -= 1
            if self.ind == 0:
                self.res = node.val
                return
            bst(node.right)
        bst(root)
        return self.res