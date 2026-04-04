# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sumToCnt = {}

        def dfs(node) -> int:
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            curSum = node.val + l + r
            self.sumToCnt[curSum] = self.sumToCnt.get(curSum, 0) + 1
            return curSum

        dfs(root)
        maxFreq = max(self.sumToCnt.values())
        return [k for k, val in self.sumToCnt.items() if val == maxFreq]
            
