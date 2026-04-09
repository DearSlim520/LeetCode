# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.prev = float('inf')
        def searchMin(node):
            if not node:
                return
            
            searchMin(node.left)
            self.minDiff = min(self.minDiff, abs(node.val - self.prev))
            self.prev = node.val
            searchMin(node.right)

        searchMin(root)
        return self.minDiff