class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        dp=[[False]*n for _ in range(n)]
        res=s[0]
        for length in range(n): #斜着遍历，斜着遍历的长度从0到n
            for i in range(n):
                j=i+length # 列的值为长度+起始的i的位置
                if j>=n:
                    break
                if length==0: # i==j的情况
                    dp[i][j]=True
                elif length==1: # 两个元素的情况
                    dp[i][j]=s[i]==s[j]
                else:
                    dp[i][j]=dp[i+1][j-1] and (s[i]==s[j])
                if dp[i][j] and len(res)<length+1:
                    res=s[i:j+1]
        return res