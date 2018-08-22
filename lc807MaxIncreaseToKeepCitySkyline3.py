class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxRow = [max(item) for item in grid]
        maxCol = [max(item) for item in zip(*grid)]

        return sum([min(maxRow[r], maxCol[c]) - val
                    for r, row in enumerate(grid)
                    for c, val in enumerate(row)])