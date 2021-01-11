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
def dijkstra(aGraph,start,n):
    pq=[]
    for i in range(n):
        if i==start:
            heapq.heappush(pq,0)
        else:
            heapq.heappush(pq,sys.maxsize)
    while pq:
        current=heapq.heappop(pq)

