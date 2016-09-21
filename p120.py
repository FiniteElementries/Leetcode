class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum = triangle[:]
        sum[-1] = triangle [-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(sum[i])):
                sum[i][j] = min(sum[i+1][j]+triangle[i][j], sum[i+1][j+1]+triangle[i][j])

        return sum[0][0]




if __name__=="__main__":
    triangle =[
                     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                ]

    solution = Solution()
    solution.minimumTotal(triangle)