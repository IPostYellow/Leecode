"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

 

示例 1：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        # 一个数字这样弄最终会陷入循环或者变为1，那么只要用快慢指针，总会遇上
        def get_next(n):
            sums = 0
            while (n > 0):
                a = n % 10
                sums = sums + a * a
                n = n // 10
            return sums

        p1 = get_next(n)
        p2 = get_next(get_next(n))
        while p1 != p2:
            p1 = get_next(p1)
            p2 = get_next(get_next(p2))

        return p1 == 1


# 第二次
class Solution:
    def isHappy(self, n: int) -> bool:
        # 一个数字这样弄最终会陷入循环或者变为1，那么只要用快慢指针，总会遇上
        def get_next_num(n):
            res = 0
            while n > 0:
                tmp = n % 10
                res += tmp * tmp
                n = n // 10
            return res

        slow, fast = get_next_num(n), get_next_num(get_next_num(n))
        while slow != fast:  # 最终就会相遇，只是相遇的时候是1还是其他数罢了，因为99999999第一个数9后面乘亿了，肯定比你其他全部9加起来大，所以不可能到无穷大的
            slow = get_next_num(slow)
            fast = get_next_num(get_next_num(fast))

        if slow == 1:
            return True
        else:
            return False
