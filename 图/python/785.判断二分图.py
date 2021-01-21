'''
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。
示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:
graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-graph-bipartite
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution: #dfs超级慢
    def dfs(self, cur, prev, graph, used, union_find):
        '''
        graph是邻接表
        used是表示遍历过的结点
        '''
        if cur in used:
            if prev == union_find[cur]:
                return False
            return True
        union_find[cur] = not prev
        used.add(cur)
        return all([self.dfs(i, union_find[cur], graph, used, union_find) for i in graph[cur]])

    def isBipartite(self, graph: List[List[int]]) -> bool:
        union_find = [None] * len(graph)
        for i in range(len(graph)):
            used = set()
            if not self.dfs(i, True, graph, used, union_find):
                return False

        return True


""" 
graph 使用字典实现 { 顶点：连接顶点列表} 3键key是图中顶点 4值value是与顶点相连接的顶点组成的队列 5
"""
# def bfs_search(graph,start_point):
# # 顶点无效、图无效、连接顶点为空，算法结束
#     if start_point not in graph:
#         return None
#     if graph[start_point] is None:
#         return None
#     if graph[start_point] == []:
#         return None
# # 队列：存储待访问顶点
#     queue = [start_point]
# # 集合：存储已访问顶点
#     visited = set()
# # 待访问顶点队列不为空，则循环继续
#     while queue:
# # 访问队列第一个顶点
#         point = queue.pop(0)
#         if point not in visited:
# # 顶点未访问，加入已访问集合
#             visited.add(point)
# # 连接顶点队列扩充到未访问队列
# # extend() 函数用于在列表末尾一次性追加
# # 另一个序列中的多个值（用新列表扩展原来的列表）
# # graph[point]为连接顶点，去掉已访问的顶点
#         queue.extend(graph[point]-visited)
#     return visited
import queue
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for j in range(len(graph)):
            used=set()
            que=queue.Queue()
            que.put([j,True])
            union_find=[None]*len(graph)
            while(not que.empty()):
                cur,prev=que.get()
                if cur in used:
                    if prev==union_find[cur]:
                        return False
                else:
                    used.add(cur)
                    union_find[cur]=not prev
                    for i in graph[cur]:
                        que.put([i,union_find[cur]])
        return True
s=Solution2()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))