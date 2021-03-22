"""
给定一组正数数组，然后给定一个数，判断这组数中有没有和为这个数
Example 1: #
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
Example 2: #
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}
Example 3: #
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
"""


# dp方法，dp[j]为数组里有和为j的子集，dp[j]=dp[j] or dp[j-nums[i]]
def subset_sum(nums, S):
    dp = [True] + [False] * S # dp[j]为和为j的子集是否在nums中存在。很显然dp[0]=True
    for i in range(len(nums)):
        for j in range(S, nums[i] - 1, -1): # 每遍历一个数就从S开始更新dp数组
            dp[j] = dp[j] or dp[j - nums[i]]
    return dp[-1]


print(subset_sum([1, 2, 3, 7], 6))
print(subset_sum([1, 2, 7, 1, 5], 10))
print(subset_sum([1, 3, 4, 8], 6))
