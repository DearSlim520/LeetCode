# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int:
            if not root:
                return 0

            total = 0
            if root.left and not root.left.left and not root.left.right:
                total += root.left.val

            total += dfs(root.left) + dfs(root.right)

            return total
            
        return dfs(root)
            