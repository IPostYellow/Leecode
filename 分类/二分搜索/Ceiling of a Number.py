"""
给定一个升序的数组，找到刚好比给定的数字大于等于的数
Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
"""


def search_ceiling_of_a_number(arr, key):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left >> 1)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    if arr[left] >= key:
        return left
    return -1


def search_ceiling_of_a_number2(arr, key):
    if key > arr[-1]:
        return -1
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left >> 1)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return left  # 这种把不存在的情况首先就考虑了


print(search_ceiling_of_a_number([4, 6, 10], 6))
print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
print(search_ceiling_of_a_number([4, 6, 10], 17))
print(search_ceiling_of_a_number([4, 6, 10], -1))


print(search_ceiling_of_a_number2([4, 6, 10], 6))
print(search_ceiling_of_a_number2([1, 3, 8, 10, 15], 12))
print(search_ceiling_of_a_number2([4, 6, 10], 17))
print(search_ceiling_of_a_number2([4, 6, 10], -1))