"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}  # mapping: old node -> new node
        q = deque([node])
        while q:
            cur = q.popleft()
            copyNode = clones[cur]

            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val) # create copy node
                    q.append(neighbor)
                copyNode.neighbors.append(clones[neighbor])

        return clones[node]
                