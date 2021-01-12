'''
有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。
现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

示例 1：
输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释:
城市航班图如下

从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
示例 2：
输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释:
城市航班图如下
从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。

提示：
n 范围是 [1, 100]，城市标签从 0 到 n - 1
航班数量范围是 [0, n * (n - 1) / 2]
每个航班的格式 (src, dst, price)
每个航班的价格范围是 [1, 10000]
k 范围是 [0, n - 1]
航班没有重复，且不存在自环
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        agraph = defaultdict(dict)
        for i, j, k in flights:
            agraph[i][j] = k

        d = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K + 1 or cost > d.get((k, place), float('inf')):  # k代表能过几个节点，一个节点两条边
                continue
            if place == dst:
                return cost
            for next, c in agraph[place].items():
                new_cost = cost + c
                if new_cost < d.get((k + 1, place), float('inf')):
                    heapq.heappush(pq, (new_cost, k + 1, next))
                    d[(k + 1, next)] = new_cost
        return -1


s = Solution()
print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
import sys


class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        dp = [[sys.maxsize] * n for _ in range(K + 1)]
        for i, j, k in flights:
            if i == src:
                dp[0][j] = k
        for i in range(K + 1):
            for j, k, z in flights:
                dp[i][k] = min(dp[i - 1][k], dp[i][k], dp[i - 1][j] + z)

        if dp[-1][dst]<sys.maxsize:
            return dp[-1][dst]
        else:
            return -1

s = Solution2()
print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))