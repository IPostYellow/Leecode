'''
给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。

样例 1:
输入: "19:34"
输出: "19:39"
解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后。
样例 2:
输入: "23:59"
输出: "22:22"
解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-closest-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def nextClosestTime(self, time: str) -> str:
        tmp_time = time.split(":")
        number_list = []
        for i in tmp_time:
            for j in i:
                number_list.append(int(j))
        total_time = int(tmp_time[0]) * 60 + int(tmp_time[1])
        for i in range(total_time + 1, 1441):
            if (i // 600 in number_list) and (i // 60 % 10 in number_list) and (
                    i % 60 // 10 in number_list) and (i % 60 % 10 in number_list):
                return (str(i // 600) + str(i // 60 % 10) +":"+ str(i % 60 // 10) + str(
                    i % 60 % 10))
        #第二天了
        for i in range(total_time+1):
            if (i // 600 in number_list) and (i // 60 % 10 in number_list) and (
                    i % 60 // 10 in number_list) and (i % 60 % 10 in number_list):
                return (str(i // 600) + str(i // 60 % 10)+":" + str(i % 60 // 10) + str(
                    i % 60 % 10))
s = Solution()
print(s.nextClosestTime("19:23"))

#第二次
class Solution2:
    def nextClosestTime(self, time: str) -> str:

        total_number = []
        for i in range(len(time)):
            if i != 2:
                total_number.append(int(time[i]))
        t = time.split(':')
        m = int(t[0]) * 60 + int(t[1])
        for i in range(m + 1, 24 * 60 + 1):
            if (i // 600) in total_number and (i // 60 % 10) in total_number and (i % 60 // 10) in total_number and (
                    i % 60 % 10) in total_number:
                return str(i // 600) + str(i // 60 % 10) + ":" + str(i % 60 // 10) + str(i % 60 % 10)
        for i in range(0, m + 1):
            if (i // 600) in total_number and (i // 60 % 10) in total_number and (i % 60 // 10) in total_number and (
                    i % 60 % 10) in total_number:
                return str(i // 600) + str(i // 60 % 10) + ":" + str(i % 60 // 10) + str(i % 60 % 10)