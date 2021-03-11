"""
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
注意:
 nums 数组的总和是一定在 32 位有符号整数范围之内的。
示例 1:
输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:
输入: nums = [-2, -1, 2, 1], k = 1
输出: 2
解释: 子数组 [-1, 2] 和等于 1，且长度最长。
进阶:
你能使时间复杂度在 O(n) 内完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 统计前缀和，比如[1,-1,5,-2,3] k=3
        # 前缀和为[1,0,5,3,6] 此时如果直接发现有等于k的，那么就是一个，然后发现6-3=3，也就是num[i]-num[j]=k 那就说明j+1到i这段的和为k
        # [-2,-1,2,1] k=1
        # [-2,-3,-1,0]
        sum_set = defaultdict(int)
        max_len = 0
        tmp_sum = 0
        sum_array = [0] * len(nums)
        for i in range(len(nums)):
            tmp_sum += nums[i]
            sum_array[i] = tmp_sum
            if tmp_sum not in sum_set:  # 记录最长的，第一次的肯定会比较长
                sum_set[tmp_sum] = i
            if tmp_sum == k:
                max_len = max(max_len, i + 1)
            if (tmp_sum - k) in sum_set:  # num[i]-num[j]==k
                max_len = max(max_len, i - sum_set[tmp_sum - k])
        return max_len
