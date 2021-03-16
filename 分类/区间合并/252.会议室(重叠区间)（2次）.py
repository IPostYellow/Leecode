"""
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x :x[0])
        for i in range(1,len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                return False
        return True

#第二次
class Solution2:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 排序好后，观察当前的右区间和下一个的左区间是否重叠即可
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True