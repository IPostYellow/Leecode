"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 利用交换，让下标为i的数组存i+1。然后再遍历一次，如果发现下标i存的值不是i+1，则说明他是重复的值
        index=0
        res=[]
        n=len(nums)
        while index<n:
            tmp=nums[index]
            if tmp!=nums[tmp-1]:
                nums[index],nums[tmp-1]=nums[tmp-1],nums[index]
            else:
                index+=1
        for i in range(n):
            if nums[i]!=i+1:
                res.append(nums[i])
        return res