from typing import List

class Solution:

    solution = []

    def dfs(self, node, edges, pre_request_count):
        if pre_request_count[node] < 0:
            return

        pre_request_count[node] -= 1
        # check pre requests
        if pre_request_count[node] > 0:
            return

        self.solution.append(node)
        if node in edges:
            for next_node in edges[node]:
                self.dfs(next_node, edges, pre_request_count)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        self.solution = []

        edges = {}

        pre_request_count = [0] * numCourses

        end_nodes = set()

        # create graph
        for edge in prerequisites:
            start = edge[1]
            end = edge[0]
            pre_request_count[end] += 1

            end_nodes.add(end)

            if start not in edges:
                edges[start] = set()

            edges[start].add(end)

        for item in range(numCourses):
            if item not in end_nodes:
                self.dfs(item, edges, pre_request_count)

        for item in pre_request_count:
            if item > 0:
                return []
        return self.solution

if __name__ == '__main__':
    s = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]

    numCourses = 3
    prerequisites = [[1, 0]]

    # numCourses = 3
    # prerequisites = [[1,0],[1,2],[0,1]]

    print(s.findOrder(numCourses, prerequisites))