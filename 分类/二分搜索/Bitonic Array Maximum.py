"""给定一个严格先递增后递减的数组，找到递增变递减的那个变点
Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10
"""


def find_max_in_bitonic_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left >> 1)
        if arr[mid] > arr[mid + 1]:  # 如果处于递减的位置，则把区间放前面
            right = mid
        else:  # 如果处于递增的位置，则把区间放后面
            left = mid + 1
    return arr[right]


print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
print(find_max_in_bitonic_array([3, 8, 3, 1]))
print(find_max_in_bitonic_array([1, 3, 8, 12]))
print(find_max_in_bitonic_array([10, 9, 8]))
