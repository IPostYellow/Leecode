"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3：

输入：nums = [1,1]
输出：1
示例 4：

输入：nums = [1,1,2]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 通过交换让下标为i的位置存储i+1。之后再遍历一遍，若发现i存的不是i+1，说明i存的是重复的
        index=0
        n=len(nums)
        while index<n:
            if nums[index]!=nums[nums[index]-1]:
                tmp=nums[index]
                nums[index],nums[tmp-1]=nums[tmp-1],nums[index]
            else:
                index+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return nums[i]

s=Solution()
print(s.findDuplicate([1,3,4,2,2]))