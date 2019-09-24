from typing import List


class Solution:

    def connect(self, u, v, arr):
        if arr[u] == 0 and arr[v] == 0:
            # new union group
            arr[u] = u
            arr[v] = u
        else:

            # attach new item to group
            if arr[v] == 0:
                arr[v] = u
            elif arr[u] == 0:
                arr[u] = v
            else:

                # connect ancestors
                k = u
                while k != arr[k]:
                    k = arr[k]

                k2 = v
                while k2 != arr[k2]:
                    k2 = arr[k2]

                if k == k2:
                    return [u, v]
                else:
                    arr[k2] = k

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = 0
        for edge in edges:
            N = max(N, edge[1])

        arr = [0] * (N + 1)

        for edge in edges:
            result = self.connect(edge[0], edge[1], arr)
            if result is not None:
                return result


if __name__ == '__main__':
    s = Solution()

    edges = [[1, 2], [1, 3], [2, 3]]

    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

    # edges = [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]

    # edges = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]

    print(s.findRedundantConnection(edges))
