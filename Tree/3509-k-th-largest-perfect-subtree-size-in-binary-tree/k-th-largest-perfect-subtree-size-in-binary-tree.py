# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node) -> int:
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            if l == r and l != -1 and r != -1:
                cur = 1 + l + r
                res.append(cur)
                return cur
            return -1

        dfs(root)
        res.sort(reverse=True)
        return res[k-1] if len(res) >= k else -1