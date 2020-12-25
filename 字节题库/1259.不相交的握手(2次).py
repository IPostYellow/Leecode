class Solution:
    def numberOfWays(self, num_people: int) -> int:
        mods=10**9+7
        dp=[0]*(num_people+1)
        dp[0]=0
        dp[2]=1
        for i in range(4,num_people+1,2):
            sums=0
            for k in range(2,i,2):
                sums+=dp[k-2]*dp[i-k]
            dp[i]=(dp[i-2]*2+sums)%mods
        return dp[-1]

s=Solution()
print(s.numberOfWays(4))

#第二次
class Solution_2:
    def numberOfWays(self, num_people: int) -> int:
        if num_people<4:
            return 1
        dp=[0]*(num_people+1)
        dp[2]=1
        mod=int(1e9+7)
        for i in range(4,num_people+1,2):
            dp[i]+=dp[i-2]*2
            for k in range(4,i,2):
                dp[i]=(dp[i]+dp[i-k]*dp[k-2])%mod
        return dp[-1]