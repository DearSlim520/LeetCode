# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        tree1 = set()
        
        # preorder dfs
        def dfs(root):
            nonlocal tree1
            if not root:
                return
            tree1.add(root.val)
            dfs(root.left)
            dfs(root.right)
            return

        def search(root) -> bool:
            if not root:
                return False
            if target - root.val in tree1:
                return True
            return search(root.left) or search(root.right)
        
        dfs(root1)
        return search(root2)