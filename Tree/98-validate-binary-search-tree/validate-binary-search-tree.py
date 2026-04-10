# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def isValid(node)->bool:
            if not node:
                return True
            l = isValid(node.left)
            if node.val <= self.prev:
                return False
            self.prev = node.val
            r = isValid(node.right)

            return l and r

        return isValid(root)