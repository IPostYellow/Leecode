"""
给定一个无限的（或者不知道尺寸的数组）升序数组，判断给定给定的值是否存在于数组内
Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.
Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
Example 3:

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.
Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.
"""
import math


class ArrayReader:  # 由于无法定义无限长度或者不定长度的数组，所以定义一个类来模拟，当超过给定数组的下标的时候返回无限大，也就是超过给定的数组后面的值都是无穷大
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinte_array(reader, key):
    # 不断扩大自己的范围，直到获取到的下标值大于key的值为止。
    start, end = 0, 1
    while reader.get(end) < key:  # 若结尾小于key值，则把start置为end后一位，然后end移动到两倍差距位置
        newStart = end + 1
        end += (end - start + 1) * 2  # 这里可以自己想多少位置合适
        start = newStart
    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start >> 1)
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:
            return mid
    return -1


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search_in_infinte_array(reader, 16))
print(search_in_infinte_array(reader, 11))
reader = ArrayReader([1, 3, 8, 10, 15])
print(search_in_infinte_array(reader, 15))
print(search_in_infinte_array(reader, 200))
