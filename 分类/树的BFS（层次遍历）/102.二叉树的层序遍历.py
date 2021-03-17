"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bfs
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]  # 借助一个队列来实现
        res = []
        while que:
            size = len(que)  # 记录每层的节点数
            local_res = []
            for i in range(size):
                tmp = que.pop(0)
                local_res.append(tmp.val)
                if tmp.left:
                    que.append(tmp.left)
                if tmp.right:
                    que.append(tmp.right)
            res.append(local_res)
        return res


# 这题dfs也能做，但是要记录当前层次，不够简单
class Solution2:
    # dfs
    def __init__(self):
        self.res = []
        self.max_level = 0

    def dfs(self, root, level):
        # 因为这里dfs每次都是先遍历左边的点再遍历右边的点的，所以self.res里的顺序天然就是按序的
        if not root:
            return
        self.res.append((root.val, level))
        if level > self.max_level:
            self.max_level = level
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        self.dfs(root, 1)
        res = [[] for _ in range(self.max_level)]
        for i in self.res:
            val, level = i
            res[level - 1].append(val)
        return res
