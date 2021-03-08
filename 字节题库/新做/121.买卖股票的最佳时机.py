class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp00=0
        dp01=-prices[0]
        for i in range(1,len(prices)):
            dp00,dp01=max(dp00,dp01+prices[i]),max(dp01,-prices[i])

        return dp00