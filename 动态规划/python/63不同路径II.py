'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
网格中的障碍物和空位置分别用 1 和 0 来表示。
'''


class Solution: #36ms,13.5mb
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for i in range(n)] for j in range(m)]
        flag = 0
        for i in range(m):
            if obstacleGrid[i][0] != 1 and flag == 0:
                f[i][0] = 1
            else:
                f[i][0] = 0
                flag = 1
        flag = 0
        for i in range(n):
            if obstacleGrid[0][i] != 1 and flag == 0:
                f[0][i] = 1
            else:
                f[0][i] = 0
                flag = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    f[i][j]=f[i-1][j]+f[i][j-1]

        return f[m-1][n-1]

s=Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
