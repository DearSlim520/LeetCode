# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, leftLen, rightLen):
            if not node:
                return
            self.res = max(self.res, leftLen, rightLen)
            dfs(node.left, rightLen + 1, 0)
            dfs(node.right, 0, leftLen + 1)
            return 

        dfs(root, 0, 0)
        return self.res