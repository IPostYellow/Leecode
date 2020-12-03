'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0
示例 4：
输入：coins = [1], amount = 1
输出：1
示例 5：
输入：coins = [1], amount = 2
输出：2
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:  # 1192ms,13.6mb
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [-1 for i in range(amount + 1)]
        f[0] = 0
        for i in range(1, amount + 1):
            tmp = []
            for j in coins:
                if i - j >= 0 and f[i - j] != -1:
                    tmp.append(f[i - j])
            if tmp == []:
                f[i] = -1
            else:
                f[i] = min(tmp) + 1
        return f[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))


class Solution2:  # [3,7,405,436]超时
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = []

        def backtrack(start, sum, track):

            for i in range(start, len(coins)):
                if sum + coins[i] == amount:
                    res.append(len(track) + 1)
                    return
                elif sum + coins[i] < amount:
                    backtrack(i, sum + coins[i], track + [coins[i]])
                elif sum + coins[i] > amount:
                    return

        backtrack(0, 0, [])
        if res == []:
            return -1
        else:
            return min(res)


s = Solution2()
print(s.coinChange([3, 7, 405, 436], 8839))
