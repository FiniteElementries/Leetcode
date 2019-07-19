class Solution(object):

    def spread_neighbor(self, i, j, grid, island_count):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] != 1:
            return
        grid[i][j] = island_count

        self.spread_neighbor(i - 1, j, grid, island_count)
        self.spread_neighbor(i + 1, j, grid, island_count)
        self.spread_neighbor(i, j - 1, grid, island_count)
        self.spread_neighbor(i, j + 1, grid, island_count)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                grid[i][j] = int(grid[i][j])

        num_island = 2
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    num_island += 1
                    self.spread_neighbor(i, j, grid, num_island)

        return num_island - 2


if __name__ == '__main__':
    s = Solution()

    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

    # grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

    grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    print(s.numIslands(grid))
