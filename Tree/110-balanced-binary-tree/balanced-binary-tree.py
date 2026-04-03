# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDiff = 0
        def dfs(node, depth):
            if not node:
                return depth
            depth += 1
            l = dfs(node.left, depth)
            r = dfs(node.right, depth)
            self.maxDiff = max(self.maxDiff, abs(l - r))
            return max(l, r)

        dfs(root, 1)
        return self.maxDiff <= 1