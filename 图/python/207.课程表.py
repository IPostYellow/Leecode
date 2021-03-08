'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：
输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def dfs(self,cur,union_find,graph):
        if union_find[cur]==-1: #-1表示之前别的路上访问过了，这样下次从另一个结点开始就直接不用访问了
            return True
        if union_find[cur]==1: #1表示在这次DFS中遍历了遍历过的结点，说明有环存在
            return False
        union_find[cur]=1
        for i in graph[cur]:
            if not self.dfs(i,union_find,graph):
                return False
        union_find[cur]=-1
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for cur,pre in prerequisites:
            graph[pre].append(cur)
        union_find=[0]*numCourses
        for i in range(numCourses):
            if not self.dfs(i,union_find,graph):
                return False
        return True