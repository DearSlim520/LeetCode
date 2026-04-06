# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.seen = {}
        def dfs(node, height):
            if not node:
                return
            
            if height not in self.seen:
                self.seen[height] = node.val
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)
            return

        dfs(root, 0)
        print
        return list(self.seen.values())