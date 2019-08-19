from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        aux = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for j in range(0, len(matrix[0])):
            aux[0][j] = int(matrix[0][j])

        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                val = int(matrix[i][j])
                if val!=0:
                    aux[i][j] = aux[i-1][j] + int(matrix[i][j])
                else:
                    aux[i][j] = 0

        max_area = 0
        for i in range(0, len(aux)):
            for j in range(0, len(aux[0])):
                count = 0
                for x in range(j, -1, -1):
                    if aux[i][x] < aux[i][j]:
                        break
                    count += 1

                for x in range(j+1, len(aux[0])):
                    if aux[i][x] < aux[i][j]:
                        break
                    count += 1

                area = aux[i][j] * count
                max_area = max(max_area, area)
        return max_area





if __name__ == '__main__':
    s = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    print(s.maximalRectangle(matrix))
