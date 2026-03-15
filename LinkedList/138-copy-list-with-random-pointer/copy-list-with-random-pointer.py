"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        cur = head
        p = dummy
        old_to_new = {}

        # create new nodes
        while cur:
            newNode = Node(cur.val)
            old_to_new[cur] = newNode
            p.next = newNode
            p = p.next
            cur = cur.next

        cur = head
        while cur:
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return dummy.next