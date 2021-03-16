"""
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
说明:

0 < nums.length <= 50000
0 < nums[i] < 1000
0 <= k < 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: #一堆大于等于1的数组不可能乘出小于1的值
            return 0
        left,right=0,0#记录当前子数组的头尾
        tmp_sub=1
        ans=0
        while right<len(nums):
            tmp_sub*=nums[right]
            while tmp_sub>=k:
                tmp_sub/=nums[left]
                left+=1
            ans=ans+right-left+1 # 10 第一次就成了 然后到[10,5]的时候，有[10,5] 和[5] right-left=2,到[10,5,2]的时候，有[10,5,2]和[2]和[5,2],到[10,5,2,6]的时候，有[10,5,2,6],[5,2,6],[2,6],[6],就是right到left每前一个都成立
            right+=1
        return ans

#第二次
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: #没有自然数的乘积会小于1
            return 0

        # 和和的异曲同工
        tmp_sub=1
        left,right=0,0
        ans=0
        while right<len(nums):
            tmp_sub*=nums[right]
            while tmp_sub>=k:
                tmp_sub/=nums[left]
                left+=1
            ans=ans+right-left+1 # [10] 1个 [10,5]->[10,5][5]两个 [10,5,2]->[10,5,2] [5,2] [2] 3个
            right+=1
        return ans