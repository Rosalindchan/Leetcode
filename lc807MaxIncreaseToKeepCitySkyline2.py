class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        listtb = []
        listlr = []
        for val1 in grid:
            max = val1[0]
            for x in val1:
                max = max if max >= x else x
            listtb.append(max)
        for i in range(len(grid[0])):
            max = grid[0][i]
            for x in range(len(grid)):
                max = max if max >= grid[x][i] else grid[x][i]
            listlr.append(max)

        sum = 0
        for i in range(len(grid)):
            for x in range(len(grid[0])):
                min = listtb[x] if listtb[x] < listlr[i] else listlr[i]
                sum = sum + min - grid[i][x]
        return sum