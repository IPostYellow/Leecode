'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:#108ms,14mb
    def solveNQueens(self, n: int):
        cheer = [["." for j in range(n)] for i in range(n)]
        result = []

        def trackback(row, cheer):
            if row == n:
                result.append([''.join(s) for s in cheer])
                return
            for col in range(n):
                if not isValid(row, col, cheer):
                    continue
                cheer[row][col] = 'Q'
                trackback(row + 1, cheer)
                cheer[row][col] = '.'

        def isValid(row, col, cheer):
            tp_row = row - 1
            tp_col = col - 1
            while (tp_col >= 0 and tp_row >= 0):  # 正对角线
                if cheer[tp_row][tp_col] == 'Q':
                    return False
                tp_row -= 1
                tp_col -= 1
            tp_row = row - 1
            tp_col = col + 1
            while (tp_row >= 0 and tp_col < len(cheer)): #逆对角线
                if cheer[tp_row][tp_col] == 'Q':
                    return False
                tp_row -= 1
                tp_col += 1
            for i in range(0, row):
                if cheer[i][col] == 'Q':
                    return False
            return True

        trackback(0,cheer)
        return result

S=Solution()
res=S.solveNQueens(4)
for i in res:
    for j in i:
        print(j)
    print('-'*80)