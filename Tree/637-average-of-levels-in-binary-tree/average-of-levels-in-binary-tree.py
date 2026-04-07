# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.total = {}
        self.count = {}

        def getAvg(node, height):
            if not node:
                return
            self.total[height] = self.total.get(height, 0) + node.val
            self.count[height] = self.count.get(height, 0) + 1

            getAvg(node.left, height + 1)
            getAvg(node.right, height + 1)

        getAvg(root, 0)
        res = []
        for h in self.total:
            res.append(round(self.total[h] / self.count[h], 5))

        return res