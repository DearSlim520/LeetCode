# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left > right:
                return None
            ind = (left + right)//2
            newRoot = TreeNode(nums[ind])
            newRoot.left = dfs(left, ind-1)
            newRoot.right = dfs(ind+1, right)

            return newRoot

        return dfs(0, len(nums) - 1)