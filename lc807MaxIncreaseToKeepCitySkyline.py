class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l=len(grid)
        ver=[grid[0][j]for j in range(l)]#数组竖直方向（即顶部，底部）
        hor=[x[0] for x in grid]#数组水平方向（即左侧，右侧）
        result=0

        #求hor[]与ver[]
        for i in range(l):
            for j in range(l):
                if grid[i][j]>hor[i]:
                    hor[i]=grid[i][j]
                if grid[j][i]>ver[i]:
                    ver[i]=grid[j][i]

        for i in range(l):
            for j in range(l):
                if (grid[i][j] !=ver[j]) and (grid[i][j] != hor[i]):
                    result=result+min(hor[i],ver[j])-grid[i][j]
        return result