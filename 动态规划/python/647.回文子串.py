'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''


class Solution:  # 496ms,21.8mb
    def countSubstrings(self, s: str) -> int:
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        count = 0
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if j == i + 1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                elif j == i + 1 and s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = (dp[i + 1][j - 1]) and (s[i] == s[j])
                    if dp[i][j]:
                        count += 1
        return count


class Solution2:  # 508ms,22.2mb
    def countSubstrings(self, s: str) -> int:
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        count = 0
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        for l in range(2, len(s)):
            for i in range(0, len(s)):
                j = l + i
                if j<len(s):
                    dp[i][j] = (dp[i + 1][j - 1]) and (s[i] == s[j])
                    if dp[i][j]:
                        count += 1
        return count


s = Solution2()
print(s.countSubstrings('aaaaa'))
