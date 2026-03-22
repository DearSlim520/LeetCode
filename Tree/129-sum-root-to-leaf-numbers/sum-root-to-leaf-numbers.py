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
            if not root.left and not root.right:
                return track * 10 + root.val
            
            tl = traverse(root.left, track * 10 + root.val)
            tr = traverse(root.right, track * 10 + root.val)

            return tl + tr

        return traverse(root, track)