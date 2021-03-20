"""
给定一个排好序的数组，然后给出一个目标值。返回这个目标值在数组中的下标（注意排序数组可能是升序也可能是降序）
Input: [4, 6, 10], key = 10
Output: 2
Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Input: [10, 6, 4], key = 10
Output: 0
Input: [10, 6, 4], key = 4
Output: 2
"""


def binary_search(arr, key):
    if not arr:
        return -1
    if len(arr) == 1:
        return arr[0]
    left, right = 0, len(arr) - 1
    asc = arr[0] < arr[1]
    if asc:
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid] == key:
                return mid
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
    else:
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid] == key:
                return mid
            if arr[mid] < key:
                right = mid - 1
            else:
                left = mid + 1
    return -1


print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([10, 6, 4], 10))
print(binary_search([10, 6, 4], 4))
print(binary_search([6, 5, 3], 1))
