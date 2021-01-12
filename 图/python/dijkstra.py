import sys
import heapq

Edge = [
    [0, 50, 10, float('inf'), 70, float('inf')],
    [float('inf'), 0, 15, float('inf'), 10, float('inf')],
    [20, float('inf'), 0, 15, float('inf'), float('inf')],
    [float('inf'), 20, float('inf'), 0, 35, float('inf')],
    [float('inf'), float('inf'), float('inf'), 30, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 3, float('inf'), 0]
]
from collections import defaultdict

dic = defaultdict(dict)
for i in range(len(Edge)):
    for j in range(len(Edge)):
        if i != j and Edge[i][j] != float('inf'):
            dic[i][j] = Edge[i][j]
print(dic)


class Solution(object):
    def findCheapestPrice(self, n, flights, start, end, K):
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}  # 存遍历过的顶点的cost，迪杰斯特拉的d数组
        pq = [(0, 0, start)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            print(best.get((k, place), float('inf')))
            if k > K + 1 or cost > best.get((k, place), float('inf')):
                continue
            if place == end:
                return cost
            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best.get((k + 1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k + 1, nei))
                    best[k + 1, nei] = newcost

        return -1


s = Solution()
s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
