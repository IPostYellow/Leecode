"""
给定一个全是小写字母升序数组，找到大于给定的字母的最小字母。（假设26个字母是个环，也就是说a是比z大的）
Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""


def search_next_letter(letters, key):
    """本质上和数的二分查找是一样的，区别在于他是个环"""
    n = len(letters)
    if key >= letters[n - 1]:  # 解环
        return letters[0]
    if key < letters[0]:
        return letters[0]
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left >> 1)
        if letters[mid] <= key:
            left = mid + 1
        else:
            right = mid  # 因为这个mid大于key的话，可能还是答案，所以这里是mid
    return letters[left]


print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
print(search_next_letter(['s','z'], 'b'))
