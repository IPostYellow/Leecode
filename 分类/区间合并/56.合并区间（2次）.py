"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0]) #排序保证了左边界，接下来只要考虑右边界就可以了
        ans=[]
        for q in intervals:
            if not ans or ans[-1][1]<q[0]: #最后的右边界都比下一个的左边界小，说明可以添加到数组里了
                ans.append(q)
            else:
                ans[-1][1]=max(ans[-1][1],q[1]) #右边界比q[0]大，则说明可以合并
        return ans

# 第二次
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 首先排序，保证左边界是有序的，这样可以减少考虑的变量
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for i in range(len(intervals)):
            if not ans or ans[-1][1]<intervals[i][0]: # 新的左边界都比答案里的右边界大，说明可以直接放进去
                ans.append(intervals[i])
            elif ans[-1][1] >= intervals[i][0]: # 说明intervals起码有一部分在ans尾端的区间内
                ans[-1][1]=max(ans[-1][1],intervals[i][1]) # 对比取最大的那个区间
        return ans