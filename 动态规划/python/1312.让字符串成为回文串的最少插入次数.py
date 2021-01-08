class Solution:#动态规划
    def minInsertions(self, s: str) -> int:
        dp=[[0]*len(s) for _ in range(len(s))]
        for jj in range(1,len(s)):
            for i in range(len(s)-jj):
                j=i+jj
                if s[i]==s[j]:
                    dp[i][j]=min(dp[i+1][j-1],dp[i+1][j]+1,dp[i][j-1]+1)
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j-1])+1
        return dp[0][-1]

class Solution2:#回溯 超时
    def is_huiwen(self,s):
        left,right=0,len(s)-1
        while(left<right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                l=self.is_huiwen(s[left+1:right+1])
                r=self.is_huiwen(s[left:right])
                return min(l,r)+1
        return 0
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        return self.is_huiwen(s)