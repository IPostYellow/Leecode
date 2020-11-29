'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:# 112ms,13.6mb
    def __init__(self):
        self.result = 0

    def totalNQueens(self, n: int) -> int:
        cheer = [["." for i in range(n)] for j in range(n)]

        def trackback(row, cheer):
            if row == n:
                self.result += 1
                return
            for i in range(n):
                if not isValid(row, i, cheer):
                    continue
                cheer[row][i] = 'Q'
                trackback(row + 1, cheer)
                cheer[row][i] = '.'

        def isValid(row, col, cheer):
            tp_row = row - 1
            tp_col = col - 1
            while (tp_row >= 0 and tp_col >= 0):
                if cheer[tp_row][tp_col] == 'Q':
                    return False
                tp_row -= 1
                tp_col -= 1

            tp_row = row - 1
            tp_col = col + 1
            while (tp_row >= 0 and tp_col < n):
                if cheer[tp_row][tp_col] == 'Q':
                    return False
                tp_row -= 1
                tp_col += 1

            for i in range(row):
                if cheer[i][col] == 'Q':
                    return False
            return True

        trackback(0, cheer)
        return self.result