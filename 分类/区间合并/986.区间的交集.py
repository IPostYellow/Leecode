"""
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

示例 1：
输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
示例 2：
输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
示例 3：
输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]
示例 4：
输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interval-list-intersections
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 最傻逼的办法就是将第二个列表中的每一个都拿去比对，找出重复的
        # 可以使用两个指针，对比当前区间的大小
        # 比如firstList = [[0,2],[5,10],[13,23],[24,25]]
        #    secondList = [[1,5],[8,12],[15,24],[25,26]]
        # 可以看到第一个[0,2] [1,5] 包含的区间应该为[0,5]，其中交集部分就是左端点最大的和右端点最小的那部分。
        # 然后[0,2]要向前移动
        # [5,10] [1,5] 包含的区间为[1,10]，交集部分为左端点的最大和右端点的最小，就是[5,5],然后第二个列表移动
        # [5,10] [8,12] 交集部分为左端点最大和右端点最小
        p1, p2 = 0, 0  # 索引两个列表
        ans = []
        while p1 < len(firstList) and p2 < len(secondList):

            tmp_l = max(firstList[p1][0], secondList[p2][0])
            tmp_r = min(firstList[p1][1], secondList[p2][1])

            if tmp_l <= tmp_r:
                ans.append([tmp_l, tmp_r])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return ans
