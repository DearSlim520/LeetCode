# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        track = 0

        def traverse(root, track):
            if not root:
                return 0

            current = track * 10 + root.val
            if not root.left and not root.right:
                return current
            
            tl = traverse(root.left, current)
            tr = traverse(root.right, current)

            return tl + tr

        return traverse(root, track)