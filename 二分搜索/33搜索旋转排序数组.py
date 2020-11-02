'''
给你一个升序排列的整数数组 nums ，和一个整数 target 。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，
如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：
输入：nums = [1], target = 0
输出：-1
 
提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:  # 36ms,13.7mb
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:  # 判断mid位置是在递增序列上还是在先递增后递减的序列上
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
