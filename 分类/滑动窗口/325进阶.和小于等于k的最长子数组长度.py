"""
给定一个数组 nums 和一个目标值 k，找到和小于等于 k 的最长子数组长度。
如果不存在任意一个符合要求的子数组，则返回 0。
"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 统计前缀和，比如[1,-1,5,-2,3] k=3
        # 前缀和为[1,0,5,3,6] 此时如果直接发现有小于等于k的，就是1,0,3，5>3,6>3 ，那么在他们之前可能有和小于等于3的
        # 如6-5<=3 则说明从5到的6的和是小于等于3的。即-2+3<=3
        sum_set=[0]*len(nums) # 存储值
        tmp_sum=0
        max_len=0
        for i in range(len(nums)):
            tmp_sum+=nums[i]
            sum_set[i]=tmp_sum
            if tmp_sum<=k:
                max_len=max(max_len,i+1)
            if (tmp_sum>k):
                for j in range(0,i):
                    if tmp_sum-sum_set[j]<=k:
                        max_len=max(max_len,i-j)
        return max_len

# 第二次
class Solution2:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len=0
        sum_array=[0]*len(nums)
        tmp_sum=0
        for i in range(len(nums)):
            tmp_sum+=nums[i]
            sum_array[i]=tmp_sum
            if tmp_sum<=k:
                max_len=max(max_len,i+1)
            else:
                for j in range(i):
                    if sum_array[i]-sum_array[j]<=k:
                        max_len=max(max_len,i-j)
                        break
        return max_len
