"""
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    # bfs做，遇到奇数层就队列出队，遇到偶数层就栈出栈
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        res = []
        while len(que) != 0:
            size = len(que)
            level_ans = []
            for i in range(size):
                tmp = que.popleft()
                level_ans.append(tmp.val)
                if tmp.left:
                    que.append(tmp.left)
                if tmp.right:
                    que.append(tmp.right)
            res.append(level_ans)
        return res[::-1]  # 层次遍历后再逆转就好了
