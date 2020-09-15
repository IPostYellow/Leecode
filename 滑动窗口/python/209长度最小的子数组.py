# coding=utf-8
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的
长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
执行用时：
44 ms, 在所有 Python3 提交中击败了97.77%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了71.65%
的用户'''
class Solution:
    def minSubArrayLen(self,s,nums):
        windowsize = len(nums) + 1
        cursum = 0
        left = 0
        right = 0
        while (right < len(nums)):
            cursum += nums[right]
            while (left<=right and cursum>=s):
                if windowsize > right - left + 1:
                    windowsize = right - left + 1
                    ansl = left
                    ansr = right
                cursum-=nums[left]
                left+=1
            right+=1
        if windowsize==len(nums)+1:
            return 0
        else:
            return windowsize

s=Solution()
nums=[2,3,1,2,4,3]
print(s.minSubArrayLen(s=7,nums=nums))