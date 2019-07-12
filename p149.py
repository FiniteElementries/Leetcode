from typing import List


class Solution:

    def gcd(self, a, b):
        r = a % b

        if r == 0:
            return b

        return self.gcd(b, r)

    def slope_between(self, i, j, points):
        if points[j][0] - points[i][0] == 0:
            return "inf"
        else:
            diffx = points[i][0] - points[j][0]
            diffy = points[i][1] - points[j][1]

            hcf = self.gcd(abs(diffy), abs(diffx))

            if hcf != 0:
                diffx /= hcf
                diffy /= hcf

            if (diffy <= 0 and diffx <= 0) or (diffy >= 0 and diffx >= 0):
                return f"{abs(diffy)}_{abs(diffx)}"
            else:
                return f"-{abs(diffy)}_{abs(diffx)}"

            # return float(points[j][1] - points[i][1]) / float(points[j][0] - points[i][0])

    def maxPointsFor(self, i, points):
        ks = {}
        same_points_count = 1
        for j in range(i + 1, len(points)):
            if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                same_points_count += 1
                continue

            k = self.slope_between(i, j, points)
            if k not in ks:
                ks[k] = []
            ks[k].append(j)

        max_slope = 0
        for k, v in ks.items():
            l = len(v)
            if l > max_slope:
                max_slope = l

        return max_slope + same_points_count

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        max_points = 1

        for i in range(0, len(points)):
            coliner_count = self.maxPointsFor(i, points)
            max_points = max(coliner_count, max_points)
        return max_points


if __name__ == "__main__":
    s = Solution()

    points = [[1, 1], [2, 2], [3, 3]]

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

    points = [[0, 0], [1, 1], [0, 0]]

    points = [[0, 0], [0, 0]]

    # points = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
    points = [[1, 1], [2, 2], [3, 3]]

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

    points = [[0, 0], [1, 1], [1, -1]]

    print(s.maxPoints(points))
