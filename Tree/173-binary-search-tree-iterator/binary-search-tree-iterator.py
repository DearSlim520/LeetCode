# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.push_to_left(root)

    def push_to_left(self, node):
        while node:
            self.stk.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stk.pop()
        if node.right:
            self.push_to_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stk else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()