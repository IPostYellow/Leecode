import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        direcitons = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        water = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        while heap:
            bar = heapq.heappop(heap)

            for (i, j) in direcitons:
                next_x, next_y = bar[1] + i, bar[2] + j
                if self.is_valid(next_x, next_y, m, n, visited):
                    water += max(0, bar[0] - heightMap[next_x][next_y])
                    heapq.heappush(heap, (max(bar[0], heightMap[next_x][next_y]), next_x, next_y))
                    visited.add((next_x, next_y))
        return water

    def is_valid(self, x, y, m, n, visited):
        if x >= 0 and y >= 0 and x < m and y < n and (x, y) not in visited:
            return True
        else:
            return False