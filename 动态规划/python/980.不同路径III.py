'''
在二维网格 grid 上，有 4 种类型的方格：
1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
示例 1：
输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
示例 2：
输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
示例 3：
输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution: #64ms,13.5mb
    def __init__(self):
        self.res=0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        step = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == 0:
                    step += 1

        def trackback(i, j, grid, cur_step):
            if i == end[0] and j == end[1] and cur_step == step+1:
                self.res += 1
                return
            grid[i][j] = -1
            if is_valid(i - 1, j, grid):
                trackback(i - 1, j, grid, cur_step + 1)
            if is_valid(i, j - 1, grid):
                trackback(i, j - 1, grid, cur_step + 1)
            if is_valid(i + 1, j, grid):
                trackback(i + 1, j, grid, cur_step + 1)
            if is_valid(i, j + 1, grid):
                trackback(i, j + 1, grid, cur_step + 1)
            grid[i][j] = 0

        def is_valid(i, j, grid):
            if i >= 0 and j >= 0 and i < row and j < col and grid[i][j] != -1:
                return True
            else:
                return False

        trackback(start[0],start[1],grid,0)
        return self.res
s=Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))