'''
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution: #dfs
    def dfs(self,cur,used,graph,stack):
        if used[cur]==-1: #该课程已经被别的DFS结点路径中学过了
            return True
        if used[cur]==1: #在当前结点的dfs中遇到遍历过的结点，说明这条dfs遍历中存在环，则不可能学完
            return False
        used[cur]=1 #将当前结点标记在当前DFS中为学完
        for e in graph[cur]:
            if not self.dfs(e,used,graph,stack):
                return False
        used[cur]=-1 #当前的DFS结束，标记cur课程为学完了的状态
        stack.append(cur)
        return True
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构造邻接表
        graph=[[] for _ in range(numCourses)]
        for cur,pre in prerequisites:
            graph[pre].append(cur)
        used=[0]*numCourses # 状态列表，0表示没有遍历过，1表示当前dfs遍历过（如果当前dfs能遇到1则说明有环），-1表示已经遍历过
        stack=[]
        for i in range(numCourses): #遍历所有结点
            if used[i]==0:
                if not self.dfs(i,used,graph,stack):
                    return []
        return stack[::-1]

from queue import Queue
class Solution2: #bfs拓扑排序，将入度为0的结点取出来
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        degree=[0]*numCourses
        que=Queue()
        result=[]
        for cur,pre in prerequisites:#构造邻接表
            graph[pre].append(cur)
            degree[cur]+=1
        for i in range(numCourses):#将入度为0的点加入队列
            if degree[i]==0:
                que.put(i)
        while (not que.empty()):#队列为空前进行bfs
            cur=que.get()
            result.append(cur)
            for i in graph[cur]:#更新当前结点cur所连接结点的入度，并将入度为0的加入队列
                degree[i]-=1
                if degree[i]==0:
                    que.put(i)

        if len(result)!=numCourses: #若没有学完所有课程，则说明不可能学完
            return []
        else:
            return result

