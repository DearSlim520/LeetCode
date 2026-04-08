# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            sz = len(q)
            total = 0
            for i in range(sz):
                cur = q.popleft()
                total += cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(round(total/sz, 5))
        
        return res