'''
我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。用户可以设置一个 “解锁模式” ，通过连接特定序列中的点，形成一系列彼此连接的线段，每个线段的端点都是序列中两个连续的点。如果满足以下两个条件，则 k 点序列是有效的解锁模式：
解锁模式中的所有点 互不相同 。
假如模式中两个连续点的线段需要经过其他点，那么要经过的点必须事先出现在序列中（已经经过），不能跨过任何还未被经过的点。
以下是一些有效和无效解锁模式的示例：

无效手势：[4,1,3,6] ，连接点 1 和点 3 时经过了未被连接过的 2 号点。
无效手势：[4,1,9,2] ，连接点 1 和点 9 时经过了未被连接过的 5 号点。
有效手势：[2,4,1,3,6] ，连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。
有效手势：[6,5,4,1,9,2] ，连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。
给你两个整数，分别为 ​​m 和 n ，那么请你统计一下有多少种 不同且有效的解锁模式 ，是 至少 需要经过 m 个点，但是 不超过 n 个点的。
两个解锁模式 不同 需满足：经过的点不同或者经过点的顺序不同。

示例 1：
输入：m = 1, n = 1
输出：9
示例 2：
输入：m = 1, n = 2
输出：65

提示：
1 <= m, n <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/android-unlock-patterns
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import threading
import queue


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            "1>3": 2,
            "3>1": 2,
            "1>7": 4,
            "7>1": 4,
            "1>9": 5,
            "9>1": 5,
            "2>8": 5,
            "8>2": 5,
            "3>7": 5,
            "7>3": 5,
            "3>9": 6,
            "9>3": 6,
            "4>6": 5,
            "6>4": 5,
            "7>9": 8,
            "9>7": 8
        }

        def trackback(used, cur, remain_step, skip):
            if remain_step == 0:
                return 1
            res = 0
            used[cur] = True
            for i in range(1, 10):
                if used[i] == False:  # 判断当前节点是否走过
                    if str(cur) + ">" + str(i) in skip:  # 判断是否跨数了
                        if used[skip[str(cur) + ">" + str(i)]] == True:  # 跨数后是否合法
                            res += trackback(used, i, remain_step - 1, skip)
                    else:
                        res += trackback(used, i, remain_step - 1, skip)

            used[cur] = False
            return res

        # used = [False] * 10
        result = 0

        def count_1_3_7_9():
            global result
            used = [False] * 10
            for i in range(m, n + 1):
                result += trackback(used, 1, i - 1, skip) * 4

        def count_2_4_6_8():
            global result
            used = [False] * 10
            for i in range(m, n + 1):
                result += trackback(used, 2, i - 1, skip) * 4

        def count_5():
            global result
            used = [False] * 10
            for i in range(m, n + 1):
                result += trackback(used, 5, i - 1, skip)

        # for i in range(m, n + 1):
        #     # t=threading.Thread()
        #     result += trackback(used, 1, i - 1, skip) * 4 # 1 3 7 9的结果个数是一样的
        #     result += trackback(used, 2, i - 1, skip) * 4 # 2 4 6 8的结果个数是一样的
        #     result += trackback(used, 5, i - 1, skip)
        t1 = threading.Thread(target=count_1_3_7_9())
        t2 = threading.Thread(target=count_2_4_6_8())
        t3 = threading.Thread(target=count_5())
        t1.start()
        t2.start()
        t3.start()
        return result


s = Solution()
print(s.numberOfPatterns(1, 2))


# 第二次
class Solution2:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            '1->3': 2,
            '3->1': 2,
            '1->7': 4,
            '7->1': 4,
            '1->9': 5,
            '9->1': 5,
            '2->8': 5,
            '8->2': 5,
            '3->7': 5,
            '7->3': 5,
            '3->9': 6,
            '9->3': 6,
            '4->6': 5,
            '6->4': 5,
            '7->9': 8,
            '9->7': 8
        }

        def count_number(cur, used, skip, rest_step):  # 从cur出发能够有多少种滑动方法
            if rest_step == 0:
                return 1
            res = 0
            used[cur] = True
            for i in range(1, 10):
                if used[i] == False:
                    if (str(cur) + "->" + str(i) not in skip) or (
                            (str(cur) + "->" + str(i) in skip) and used[skip[str(cur) + '->' + str(i)]] == True):
                        res += count_number(i, used, skip, rest_step - 1)
            used[cur] = False
            return res

        used = [False] * 10
        ans = 0
        for i in range(m, n + 1):
            for j in range(1, 10):
                ans += count_number(j, used, skip, i - 1)
        return ans


class Solution3:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            '1->3': 2,
            '3->1': 2,
            '1->7': 4,
            '7->1': 4,
            '1->9': 5,
            '9->1': 5,
            '2->8': 5,
            '8->2': 5,
            '3->7': 5,
            '7->3': 5,
            '3->9': 6,
            '9->3': 6,
            '4->6': 5,
            '6->4': 5,
            '7->9': 8,
            '9->7': 8
        }

        def count_number(cur, used, skip, rest_step):  # 从cur出发能够有多少种滑动方法
            if rest_step == 0:
                return 1
            res = 0
            used[cur] = True
            for i in range(1, 10):
                if used[i] == False:
                    if (str(cur) + "->" + str(i) not in skip) or (
                            (str(cur) + "->" + str(i) in skip) and used[skip[str(cur) + '->' + str(i)]] == True):
                        res += count_number(i, used, skip, rest_step - 1)
            used[cur] = False
            return res

        used = [False] * 10
        ans = 0
        for i in range(m, n + 1):
            ans += count_number(1, used, skip, i - 1) * 4
            ans += count_number(2, used, skip, i - 1) * 4
            ans += count_number(5, used, skip, i - 1)
        return ans


# 多线程版本
import threading


class Solution4:
    def __init__(self) -> None:
        self.res = 0

    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            "1>3": 2,
            "3>1": 2,
            "1>7": 4,
            "7>1": 4,
            "1>9": 5,
            "9>1": 5,
            "2>8": 5,
            "8>2": 5,
            "3>7": 5,
            "7>3": 5,
            "3>9": 6,
            "9>3": 6,
            "4>6": 5,
            "6>4": 5,
            "7>9": 8,
            "9>7": 8
        }

        def trackback(used, cur, remain_step, skip):
            if remain_step == 0:
                return 1
            res = 0
            used[cur] = True
            for i in range(1, 10):
                if used[i] == False:  # 判断当前节点是否走过
                    if str(cur) + ">" + str(i) in skip:  # 判断是否跨数了
                        if used[skip[str(cur) + ">" + str(i)]] == True:  # 跨数后是否合法
                            res += trackback(used, i, remain_step - 1, skip)
                    else:
                        res += trackback(used, i, remain_step - 1, skip)

            used[cur] = False
            return res

        def count_1_3_7_9():
            used = [False] * 10
            for i in range(m, n + 1):
                self.res += trackback(used, 1, i - 1, skip) * 4

        def count_2_4_6_8():
            used = [False] * 10
            for i in range(m, n + 1):
                self.res += trackback(used, 2, i - 1, skip) * 4

        def count_5():
            used = [False] * 10
            for i in range(m, n + 1):
                self.res += trackback(used, 5, i - 1, skip)

        t1 = threading.Thread(target=count_1_3_7_9)
        t2 = threading.Thread(target=count_2_4_6_8)
        t3 = threading.Thread(target=count_5)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

        return self.res

import queue
import threading
class Solution5:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            "1>3": 2,
            "3>1": 2,
            "1>7": 4,
            "7>1": 4,
            "1>9": 5,
            "9>1": 5,
            "2>8": 5,
            "8>2": 5,
            "3>7": 5,
            "7>3": 5,
            "3>9": 6,
            "9>3": 6,
            "4>6": 5,
            "6>4": 5,
            "7>9": 8,
            "9>7": 8
        }

        def trackback(used, cur, remain_step, skip):
            if remain_step == 0:
                return 1
            res = 0
            used[cur] = True
            for i in range(1, 10):
                if used[i] == False:  # 判断当前节点是否走过
                    if str(cur) + ">" + str(i) in skip:  # 判断是否跨数了
                        if used[skip[str(cur) + ">" + str(i)]] == True:  # 跨数后是否合法
                            res += trackback(used, i, remain_step - 1, skip)
                    else:
                        res += trackback(used, i, remain_step - 1, skip)

            used[cur] = False
            return res

        def count_count(start, cnt,q):
            used = [False] * 10
            result=0
            for i in range(m, n + 1):
                result += trackback(used, start, i - 1, skip) * cnt
            q.put(result)

        q = queue.Queue()
        data=[1,2,5]
        cnt=[4,4,1]
        threads=[]
        for i in range(3):
            t = threading.Thread(target=count_count,args=(data[i],cnt[i],q))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        result=0
        for _ in range(3):
            result+=q.get()
        return result