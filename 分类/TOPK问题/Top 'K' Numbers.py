"""
给定一个非排序数组，找到最大的K个数
Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""

def position(num, i, j):
    left = i
    right = j+1
    while left < right:
        left += 1
        while left < right and num[left] < num[i]:
            left += 1
        right -= 1
        while left < right and num[right] > num[i]:
            right -= 1
        if left < right:
            num[left], num[right] = num[right], num[left]
    num[i], num[right] = num[right], num[i]
    return right


def quick_sort(num, i, j):
    if i < j:
        mid = position(num, i, j)
        quick_sort(num, i, mid - 1)
        quick_sort(num, mid + 1, j)


# num = [8, 6, 1, 2, 3, 4, 5, 6, 7]
# quick_sort(num, 0, len(num) - 1)
# print(num)

# 堆排序找到topk
import heapq
def find_top_k(num,k):
    heap=[]
    for i in range(len(num)):
        if len(heap)<k:
            heapq.heappush(heap,num[i])
        else:
            if heap[0]<num[i]:
                heapq.heappushpop(heap,num[i])
    return heap

print(find_top_k([3,1,5,12,2,11],3))
print(find_top_k([5,12,11,-1,12],3))

