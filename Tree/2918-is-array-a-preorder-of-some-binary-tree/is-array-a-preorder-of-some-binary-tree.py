class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        i = 0
        n = len(nodes)
        def dfs(parentId) -> bool:
            nonlocal i
            if i >= n:
                return False
            
            targetID, targetParent = nodes[i]
            if targetParent != parentId:
                return False

            i += 1
            while i<n and nodes[i][1] == targetID:
                if not dfs(targetID):
                    return False
            return True 
                
        return dfs(-1) and i == n