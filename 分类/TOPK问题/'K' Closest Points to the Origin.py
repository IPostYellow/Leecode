"""
给定一组坐标，找到k个离原点近的坐标
Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""
from heapq import *


# 小堆
def find_closest_points(points, k):
    result = []
    new_list = []
    for i, j in points:
        new_list.append([i ** 2 + j ** 2, i, j])
    heapify(new_list)
    for i in range(k):
        tmp = heappop(new_list)
        result.append([tmp[1], tmp[2]])
    return result


print(find_closest_points([[1, 3], [3, 4], [2, -1]], 2))
print(find_closest_points([[1, 2], [1, 3]], 1))
