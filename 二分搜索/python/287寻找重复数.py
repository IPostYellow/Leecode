from typing import List
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:#60ms,14.8mb
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while (left <= right):
            mid = (left + right) >> 1
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left