"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #bfs也可以解决最短路径问题
        if not root:
            return 0
        ans=0
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            ans+=1 #进入了下一层
            for i in range(size):
                tmp=q.popleft()
                if not tmp.left and not tmp.right:
                    return ans # 遇到叶子节点就直接返回层数
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
        return ans