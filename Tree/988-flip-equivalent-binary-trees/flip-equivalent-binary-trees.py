# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            # else:
            if node1.val != node2.val:
                return False
            else:  # if root equal
                # flip
                flip = dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
                unflip = dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
                return flip or unflip
                # if node1.left and node2.left:
                #     if node1.left.val == node2.left.val:
                #         return 
                #     else:
                #         return dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
                # elif not node1.left and not node2.left:
                    
                # else: return False
            

        return dfs(root1, root2)
        