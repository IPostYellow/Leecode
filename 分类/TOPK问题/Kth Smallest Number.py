"""
给定一个未排序的数组，找到其中第K小的元素
"""


def position(num, i, j):
    tmp=num[i]
    left=i
    right=j
    while left<right:
        while left<right and num[right]>=tmp:
            right-=1
        num[left]=num[right]
        while left<right and num[left]<=tmp:
            left+=1
        num[right]=num[left]
    num[left]=tmp
    return left


def quick_sort(num, i, j, k):
    left = i
    right = j
    while left < right:
        mid = position(num, left, right)
        if mid == k - 1:  # 表示已经找到了这个数字
            return num[mid]
        elif mid > k - 1:  # 因为快排后，比mid大的都在mid右边
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_kth_smallest_number(num, k):
    return quick_sort(num,0,len(num)-1,k)


print(find_kth_smallest_number([1,5,12,2,11,5],3))
print(find_kth_smallest_number([1,5,12,2,11,5],4))
print(find_kth_smallest_number([5,12,11,-1,12],3))