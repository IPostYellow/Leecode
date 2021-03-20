"""
给定一个升序的数组找到给定数字的下标范围）
"""


def find_range(arr, key):
    """本质上就是找到坐标最小的数字和坐标最大的数字，《==》找到第一个等于key的值，找到最后一个等于key的值"""
    result = [-1, -1]
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left >> 1)
        if arr[mid] == key:
            if result[0] == -1 or result[0] > mid:
                result[0] = mid
            right = mid - 1
        if arr[mid] > key:
            right = mid - 1
        if arr[mid] < key:
            left = mid + 1

    if result[0] == -1:
        return result
    else:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if arr[mid] == key:
                if result[1] == -1 or result[1] < mid:
                    result[1] = mid
                left = mid + 1
            if arr[mid] > key:
                right = mid - 1
            if arr[mid] < key:
                left = mid + 1
    return result


print(find_range([4, 6, 6, 6, 9], 6))
print(find_range([1, 3, 8, 10, 15], 10))
print(find_range([1, 3, 8, 10, 15], 12))
