class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        preCourses = [0] * numCourses
        nextGraph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            nextGraph[b].append(a)
            preCourses[a] += 1
            
        complete = [0] * numCourses
        q = deque([i for i in range(numCourses) if preCourses[i] == 0])
        while q:
            cur = q.popleft()
            complete[cur] = 1
            for nextCourse in nextGraph[cur]:
                preCourses[nextCourse] -= 1
                if preCourses[nextCourse] == 0:
                    q.append(nextCourse)
        return True if sum(complete) == numCourses else False