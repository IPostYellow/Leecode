from typing import List
'''
给定一个按照升序排列的整数数组 nums，
和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

class Solution:#44ms,14.3MB
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) >> 1
            if nums[mid] == target:
                start = mid
            if (nums[mid] >= target):
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) >> 1
            if nums[mid] == target:
                end = mid
            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return [start, end]