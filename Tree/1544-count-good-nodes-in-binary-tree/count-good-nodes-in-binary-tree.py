# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, curMax):
            nonlocal cnt
            if not node:
                return
            if curMax <= node.val:
                cnt += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
            return

        dfs(root, float('-inf'))
        return cnt