from typing import List

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

 

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
            if nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
                if nums[index] != 1:  # 如果换完不是1，则需要回退
                    index -= 1
            index += 1

S=Solution()
nums=[2,0,2,1,1,0]
S.sortColors(nums)
print(nums)

#第二次
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 将0不断交换到左边，将2不断交换到右边
        left,right=0,len(nums)-1
        index=0
        while index<=right:
            if nums[index]==0:
                nums[index],nums[left]=nums[left],nums[index]
                left+=1
            if nums[index]==2:
                nums[index],nums[right]=nums[right],nums[index]
                right-=1
                if nums[index]!=1: #因为index是往右走的，上面那个如果出现换完以后nums[index]=0的话，无所谓，index继续走就好了，因为0就是要在index左边的
                    index-=1 # 但是如果换完是2的话，还需要继续判断这个值。所以让index原地不动
            index+=1