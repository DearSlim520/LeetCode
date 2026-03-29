# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curMin) -> int:
            if not root:
                return float('inf')

            if root.val > curMin:
                return root.val

            return min(dfs(root.left, root.val), dfs(root.right, root.val))
    
        res = dfs(root, root.val) 
        return res if res < float('inf') else -1