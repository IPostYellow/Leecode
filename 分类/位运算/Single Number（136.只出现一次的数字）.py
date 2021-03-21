"""
在一个非空数组里，每个数都出现两次，只有一个数出现一次，找到那个只出现一次的数
Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9

"""


def find_single_number(arr):
    """最简单的做法就是用哈希表存储。但是这样很费空间。
    我们可以使用XOR运算来实现这个操作
    XOR的定义，如果1^1=0 0^0=0 1^0=1 0^1=1
    满足交换律，所以77^66^77=66
    """
    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp ^= arr[i]
    return tmp


arr = [1, 4, 2, 1, 3, 2, 3]
print(find_single_number(arr))
print(find_single_number([7, 9, 7]))
print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
