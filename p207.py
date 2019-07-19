from typing import List


class Solution:

    def dfs(self, node, edges, visited):
        if visited[node] == 2:
            return True
        if visited[node] == 1:
            return False

        visited[node] = 1
        if node in edges:
            for item in edges[node]:
                if not self.dfs(item, edges, visited):
                    return False
        visited[node] = 2
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        edges = {}
        for edge in prerequisites:
            start = edge[1]
            end = edge[0]
            if start not in edges:
                edges[start] = []
            edges[start].append(end)

        visited = [0] * numCourses
        for item in range(0, numCourses):
            if not self.dfs(item, edges, visited):
                return False
        return True


if __name__ == '__main__':
    s = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]

    # numCourses = 3
    # prerequisites = [[1, 0]]

    # numCourses = 3
    # prerequisites = [[1,0],[1,2],[0,1]]

    print(s.canFinish(numCourses, prerequisites))
