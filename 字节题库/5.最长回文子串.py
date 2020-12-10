'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:  # 9980ms,22.1mb,看运气全是超时
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        res = s[0]
        dp = [[False for _, _ in enumerate(s)] for _, _ in enumerate(s)]
        for i, _ in enumerate(s):
            dp[i][i] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if j == i + 1:  # 很关键，这题就是对于长度小于等于2的回文串的判断很重要
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and (j - i + 1) > len(res):
                    res = s[i:j + 1]
        return res


s = Solution()
print(s.longestPalindrome('aaaaa'))
