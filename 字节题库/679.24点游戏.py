"""
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        def solve(nums):
            if len(nums) == 1:
                if abs(nums[0] - 24) <= 1e-6:
                    return True
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    else:
                        if i==2 and j==0:
                            print(i,j)
                        # 取出这两个数
                        newnums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        if solve(newnums + [nums[i] + nums[j]]): return True
                        if solve(newnums + [nums[i] - nums[j]]): return True
                        if solve(newnums + [nums[i] * nums[j]]): return True
                        if nums[j] != 0:
                            if solve(newnums + [nums[i] / nums[j]]):
                                return True
            return False
        return solve(nums)

s = Solution()
print(s.judgePoint24([3, 3, 8, 8]))

#第二次
