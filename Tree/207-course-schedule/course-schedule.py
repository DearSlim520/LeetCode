class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        preCoureses = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            preCoureses[a] += 1

        completed = [0] * numCourses
        q = deque([i for i in range(numCourses) if preCoureses[i] == 0])
        while q:
            cur = q.popleft()
            completed[cur] = 1
            for next_course in graph[cur]:
                preCoureses[next_course] -= 1
                if preCoureses[next_course] == 0:
                    q.append(next_course)
        return True if sum(completed) == numCourses else False