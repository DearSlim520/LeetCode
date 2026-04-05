# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod= 10**9 + 7
        self.res = 0
        def whole(node):
            if not node:
                return 0
            return whole(node.left) + whole(node.right) + node.val
        total = whole(root)
        def dfs(node) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.res = max(self.res, l * (total - l), r * (total - r))
            return l + r + node.val

        dfs(root)
        return self.res % mod