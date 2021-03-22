"""
给定一组绳子长度的数组，求绳子连接起来的最小代价
绳子连接的代价是绳子长度
哈夫曼树！用小堆实现，每次弹出最小的两个
"""
import sys
sys.setrecursionlimit(1000000)
from heapq import *
def minimum_cost_to_connect_ropes(ropeLengths):
    result=0
    newlist=[]
    for i in range(len(ropeLengths)):
        heappush(newlist,ropeLengths[i])
    while len(newlist)>1:
        tmp1=heappop(newlist)
        tmp2=heappop(newlist)
        result=result+tmp1+tmp2
        heappush(newlist,tmp1+tmp2)
    return result

print(minimum_cost_to_connect_ropes([1,3,11,5]))
print(minimum_cost_to_connect_ropes([3,4,5,6]))
print(minimum_cost_to_connect_ropes([1,3,11,5,2]))
