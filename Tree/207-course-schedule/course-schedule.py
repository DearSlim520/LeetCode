class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 这题本质是判断prerequisites里面是否存在环： 是，False； 否，True
        # create graph
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses # 0 unvisited, 1 visited, 2 complete
        def dfs(course) -> bool:
            # exits
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visited[course] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True