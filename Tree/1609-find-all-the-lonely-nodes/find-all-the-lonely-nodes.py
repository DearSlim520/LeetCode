# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, hasSibling) -> int:
            if not node:
                return
            if not hasSibling and node != root:
                res.append(node.val)
            dfs(node.left, node.right is not None)
            dfs(node.right, node.left is not None)
            return

        dfs(root, False)
        return res