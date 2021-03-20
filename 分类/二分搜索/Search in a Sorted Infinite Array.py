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


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr
    def get(self,index):
        if index>=len(self.arr):
            return math.inf
        return self.arr[index]

def search_in_infinte