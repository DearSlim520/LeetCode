# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        def dfs(node, pVal, curStep):
            if not node:
                return
            curStep += 1
            if node.val == pVal + 1:
                self.res = max(self.res, curStep)
            else:
                curStep = 1
            dfs(node.left, node.val, curStep)
            dfs(node.right, node.val, curStep)

        dfs(root, float('inf'), 1)
        return self.res    