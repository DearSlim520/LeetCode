class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0
        
        def dfs(root):
            nonlocal length
            
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            length = max(length, left_height + right_height)    # calculate diameter of the currentnode
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return length
