from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a graph to read from equations
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0/val

        # dfs: search route from starter -> end
        def dfs(node, end, seen):
            if node == end:
                return 1.0
            seen.add(node)

            for neighbor, weight in graph[node].items():
                if neighbor not in seen:
                    res = dfs(neighbor, end, seen)
                    if res != -1.0:
                        return res * weight
            return -1.0    

        # calculate all queries
        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            elif start == end:
                res.append(1.0)
            else:
                seen = set()
                res.append(dfs(start, end, seen))

        return res
        