# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        hl = self.getHeight(root.left)
        hr = self.getHeight(root.right)

        if hl == hr:
            return (1 << hl) + self.countNodes(root.right)
        else:
            return (1 << hr) + self.countNodes(root.left)

    def getHeight(self, root) -> int:
        height = 0
        while root:
            height += 1
            root = root.left
        return height

            

        