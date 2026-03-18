# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if (not t1 and t2) or (not t2 and t1):
            return False
        elif not t1 and not t2:
            return True
        
        left = self.isMirror(t1.left, t2.right)
        right = self.isMirror(t1.right, t2.left)

        return left and right and t1.val == t2.val