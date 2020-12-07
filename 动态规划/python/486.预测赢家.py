'''
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，
随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。
直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
给定一个表示分数的数组，预测玩家1是否会成为赢家。
你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：
输入：[1, 5, 2]
输出：False
解释：一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。
示例 2：
输入：[1, 5, 233, 7]
输出：True
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
 
提示：
1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于 10000000 。
如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         def trackback(i, j, flag, score1, score2):  # flag表示轮到哪个玩家选了
#             if i > j:
#                 return -1
#             else:
#                 if flag == 1:
#                     tmp1 = trackback(i + 1, j, -flag, score1 + nums[i], score2)
#                     tmp2 = trackback(i, j - 1, -flag, score1 + nums[j], score2)
#                     if tmp1>0 and tmp2>0:
#                         return max(tmp1,tmp2)
#                     elif tmp1>0 and tmp2<0:
#                         return tmp1
#                     elif tmp2>0 and tmp1<0:
#                         return tmp2
#                     else:
#                         return -1
#                 else:
#                     tmp1 = trackback(i + 1, j, -flag, score1, score2 + nums[i])
#                     tmp2 = trackback(i, j - 1, -flag, score1, score2 + nums[j])
#                     if tmp1 > 0 and tmp2 > 0:
#                         return max(tmp1, tmp2)
#                     elif tmp1 > 0 and tmp2 < 0:
#                         return tmp1
#                     elif tmp2 > 0 and tmp1 < 0:
#                         return tmp2
#                     else:
#                         return -1
#         score=trackback(0, len(nums) - 1, 1, 0, 0)
#         print(score)
#         return self.res


# 思维应该逆转，因为你选完后，就是对面选了，所以是一个减法，减去的那个值是对面选的最大的值
class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def trackback(i, j):
            if (i == j):
                return nums[i]
            picki = nums[i] - trackback(i + 1, j)
            pickj = nums[j] - trackback(i, j - 1)
            return max(picki, pickj)

        return trackback(0, len(nums) - 1) >= 0


s = Solution2()
print(s.PredictTheWinner([1, 5, 233, 7]))


class Solution3:#40ms,13.6mb
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp1 = [[0 for i in range(len(nums))] for j in range(len(nums))]
        dp2 = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            dp1[i][i] = nums[i]
            dp2[i][i] = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                left = nums[i] + dp2[i + 1][j]  # 先手的选了以后，下一次就相当于变成了后手，所以要加后手的
                right = nums[j] + dp2[i][j - 1]
                if left > right:
                    dp1[i][j] = left
                    dp2[i][j] = dp1[i + 1][j]  # 同理，这次后手的，下一次就会变成先手了
                else:
                    dp1[i][j] = right
                    dp2[i][j] = dp1[i][j - 1]
        return dp1[0][len(nums) - 1] >= dp2[0][len(nums) - 1]


s = Solution3()
print(s.PredictTheWinner([1, 5, 233, 7]))
