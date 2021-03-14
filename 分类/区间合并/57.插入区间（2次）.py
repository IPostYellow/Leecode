"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        i=0
        # 把要合并的左边放入列表
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        # 开始要合并了
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        # 把要合并的右边放入列表
        ans.append(newInterval)
        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans

#第二次
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 关键就是要把插入的区间找出来，那么要插入的左边和右边都可以保持原样
        ans=[]
        index=0
        while index<len(intervals) and intervals[index][1]<newInterval[0]:
            ans.append(intervals[index]) # 把要插入区间左边原封不动放入列表
            index+=1
        while index<len(intervals) and intervals[index][0]<=newInterval[1]: # 找到左区间都比要插入的区间的右区间大的位置
            newInterval[0]=min(newInterval[0],intervals[index][0]) # 因为最后要合并成一个区间，所以不断更新一个区间的范围即可
            newInterval[1]=max(newInterval[1],intervals[index][1])
            index+=1
        ans.append(newInterval)
        while index<len(intervals): # 把插入区间右边原封不动放入列表
            ans.append(intervals[index])
            index+=1
        return ans