# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if i == sz - 1:
                    res.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)

        return res