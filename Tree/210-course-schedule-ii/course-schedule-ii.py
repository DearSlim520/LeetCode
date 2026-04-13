class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        toUnlock = [0] * numCourses # number of courses should be take before
        for a, b in prerequisites:
            graph[b].append(a)
            toUnlock[a] += 1
        
        res = []
        q = deque([i for i in range(numCourses) if toUnlock[i] == 0])
        while q:
            cur = q.popleft()
            res.append(cur)
            for next_course in graph[cur]:
                toUnlock[next_course] -= 1
                if toUnlock[next_course] == 0:
                    q.append(next_course)
        
        return res if len(res) == numCourses else []

        