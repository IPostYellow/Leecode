from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*3 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=0
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][2])
            dp[i][2]=dp[i-1][0]+prices[i]
        return max(dp[-1][1],dp[-1][2])

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp00=-prices[0]
        dp01=0
        dp02=0
        for i in range(1,len(prices)):
            dpi0=max(dp00,dp01-prices[i])
            dpi1=max(dp01,dp02)
            dpi2=dp00+prices[i]
            dp00=dpi0
            dp01=dpi1
            dp02=dpi2
        return max(dp01,dp02)