"""
给定一个升序数组，找到最接近key值的值。
Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""


def search_min_diff_element(arr, key):
    if key < arr[0]:
        return -1
    if key > arr[-1]:
        return arr[-1]
    left, right = 0, len(arr) - 1
    while left <= right:  # 要遍历完所有数字
        mid = left + (right - left >> 1)
        if arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            return arr[mid]
    if abs(key - arr[left]) > abs(arr[right] - key):  # 看哪个更靠近
        return arr[right]
    else:
        return arr[left]


print(search_min_diff_element([4, 6, 10], 7))
print(search_min_diff_element([4, 6, 10], 4))
print(search_min_diff_element([1, 3, 8, 10, 15], 12))
print(search_min_diff_element([4, 6, 10], 17))
