'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:  # 44ms,13.8MB
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, tmp):
            if not nums:  # 结束条件。也就是得到n个数字以后
                result.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
            # 每次取去掉那个i的数，然后将其数拼起来，tmp就是已经拼好的

        backtrack(nums, [])
        return result


s = Solution()
print(s.permute([1, 2, 3]))
