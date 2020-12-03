'''
给你两个单词 word1 和 word2，请你计算出将 word1 
转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
 
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:#160ms,17.2mb
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        dp = [[0 for i in range(len_word2 + 1)] for j in range(len_word1 + 1)]
        for i in range(len_word1+1):
            dp[i][0] = i
        for i in range(len_word2+1):
            dp[0][i] = i
        for row in range(1, len_word1 + 1):
            for col in range(1, len_word2 + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1

        return dp[len_word1][len_word2]


s = Solution()
print(s.minDistance("horse", "ros"))
