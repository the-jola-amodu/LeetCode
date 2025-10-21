from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[node] = VISITING
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        