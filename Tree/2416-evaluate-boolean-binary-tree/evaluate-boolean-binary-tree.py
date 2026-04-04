# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return True if root.val == 1 else False
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        return l and r if root.val == 3 else l or r