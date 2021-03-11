"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 将问题一分为二，即sum(正)-sum(负)=target，又已知sum(正)+sum(负)=sum(总),用sum(总)替换sum(负)，得2sum(正)=target+sum(总)
        # 那原题就相当于求，有多少数字组合相加能等于sum(正)。这是一个01背包问题，使用dp来求解
        # 设dp[j]是和为j时的组合方法数，那么dp[j]的更新方法很显然如果遍历到了nums[i],dp[j]=dp[j]+dp[j-nums[i]]
        total = sum(nums)
        if S > total or (S + total) % 2 == 1:
            return 0
        pos_num = (S + total) // 2
        dp = [0] * (pos_num + 1)
        dp[0] = 1  # 装0件物品可达到和为0，有一种方法
        for i in range(len(nums)):
            for j in range(pos_num, nums[i] - 1, -1):  # 每遍历到一个nums[i]，就要更新一次dp数组
                dp[j] = dp[j] + dp[j - nums[i]]
        return dp[pos_num]
