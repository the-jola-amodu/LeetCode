from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [source]
        seen = set()
        seen.add(source)
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
        return False
        