# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.gloMax = float('-inf')
        def dfs(node) -> int:
            if not node:
                return 0

            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            self.gloMax = max(self.gloMax, node.val + l + r)
            return node.val + max(l, r)

        dfs(root)
        return self.gloMax