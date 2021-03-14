"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1 #因为是按非递减顺序排的，所以肯定在开头和末尾两头的平方肯定是有最大值的，所以逆序排列
        ans=[0]*len(nums)
        index=len(nums)-1
        while left<right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                ans[index]=nums[left]*nums[left]
                index-=1
                left+=1
            else:
                ans[index]=nums[right]*nums[right]
                index-=1
                right-=1
        ans[index]=nums[left]*nums[left]
        return ans

#第二次
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 因为已经排好序了，所以平方大的肯定在两端，所以我们从两端往中间判断就可以了
        left,right=0,len(nums)-1
        ans=[0]*len(nums)
        index=len(nums)-1 #记录答案数组的下标，从后往前存
        while left<=right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                ans[index]=nums[left]*nums[left]
                index-=1
                left+=1
            else:
                ans[index]=nums[right]*nums[right]
                index-=1
                right-=1
        return ans