"""
给定一组正数，找到和相等的两个子集
Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""


def can_partition(num):
    set2 = sum(num)
    set1 = 0

    def track_back(num, used, set1, set2):
        if set1 == set2:
            return True
        for i in range(len(num)):
            if used[i] == 0:
                used[i] = 1
                if track_back(num, used, set1 + num[i], set2 - num[i]):
                    return True
                used[i] = 0
        return False

    used = [0 for _ in range(len(num))]
    if track_back(num, used, set1, set2):
        return True
    return False
print(can_partition([1,2,3,4]))
print(can_partition([1,1,3,4,7]))
print(can_partition([2,3,4,6]))

from typing import List
# dp方法
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        sums = sums // 2
        dp = [True] + [False] * sums  # dp[j] 为数组存不存在和为j的子集，很显然dp[0]=True
        for i in range(len(nums)):
            for j in range(sums, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]] # 要么自己已经是true了，要么就是j-nums[i]加nums[i]
        return dp[-1]

