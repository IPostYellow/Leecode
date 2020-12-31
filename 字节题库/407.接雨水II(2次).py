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

#第二次
import heapq


class Solution_2:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        def Is_valid(i, j, m, n, visited):
            if i >= 0 and j >= 0 and i < m and j < n and visited[i][j] == False:
                return True
            else:
                return False
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]
        choice = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heapq.heappush(heap, (heightMap[0][0], 0, 0))
        visited[0][0] = True
        heapq.heappush(heap, (heightMap[0][n - 1], 0, n - 1))
        visited[0][n - 1] = True
        heapq.heappush(heap, (heightMap[m - 1][0], m - 1, 0))
        visited[m - 1][0] = True
        heapq.heappush(heap, (heightMap[m - 1][n - 1], m - 1, n - 1))
        visited[m - 1][n - 1] = True
        for i in range(1, m - 1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True
        water = 0
        while (heap):
            tmp = heapq.heappop(heap)
            for i, j in choice:
                next_x, next_y = tmp[1] + i, tmp[2] + j
                if Is_valid(next_x, next_y, m, n, visited):
                    water += max(0, tmp[0] - heightMap[next_x][next_y])
                    heapq.heappush(heap, (max(tmp[0], heightMap[next_x][next_y]), next_x, next_y))
                    visited[next_x][next_y] = True
        return water