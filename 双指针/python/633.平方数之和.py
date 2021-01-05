'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：
输入：c = 3
输出：false
示例 3：
输入：c = 4
输出：true
示例 4：
输入：c = 2
输出：true
示例 5：
输入：c = 1
输出：true
'''
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        N = math.floor(math.sqrt(c))
        left, right = 0, N
        while (left <= right):
            tmp = left * left + right * right
            if tmp == c:
                return True
            elif tmp < c:
                left += 1
            elif tmp > c:
                right -= 1
        return False
