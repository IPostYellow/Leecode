"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

 

进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

 

示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: #原地哈希
        # 将对应的正数换到正数-1的位置。然后从头开始遍历，如果有正数-1的位置不等于正数，这说明缺了这个正数
        # 若全都不缺，则说明数组里全都是符合1到n的正数，返回n+1
        index=0
        n=len(nums)
        while index<n:
            tmp=nums[index]
            if tmp>0 and tmp<n and nums[tmp-1]!=tmp:
                nums[tmp-1],nums[index]=nums[index],nums[tmp-1]
            else:
                index+=1
        for j in range(1,n+1):
            if nums[j-1]!=j:
                return j
        return n+1