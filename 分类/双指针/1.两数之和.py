"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 变型：如果这个nums是有序的呢？
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_num = {}  # 字典存储已经遍历过的值，用目标值减去当前值看看是否有等于遍历过的值
        for i in range(len(nums)):
            if target - nums[i] in tmp_num:
                return [tmp_num[target - nums[i]], i]
            tmp_num[nums[i]] = i
# 变型：如果这个nums是有序的呢？
class Solution2:
    def twoSum_order(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while (left<right):
            if nums[left]+nums[right]==target:
                return [left,right]
            elif nums[left]+nums[right]>target:
                right-=1
            else:
                left+=1
        return [-1,-1]

