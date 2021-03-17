"""给定一棵树，把他的所有兄弟结点连接起来（不是同一个父亲也连）"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.brother = None


class Solution:
    def LevelOrderSuccessor(self, root: TreeNode):
        if not root:
            return []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            tmp = q.popleft()
            pre = tmp
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
            for i in range(size - 1):
                tmp = q.popleft()
                pre.brother = tmp
                pre = tmp
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)

        return root


r = TreeNode(3)
rl = TreeNode(9)
rr = TreeNode(20)
rll = TreeNode(6)
rrl = TreeNode(15)
rrr = TreeNode(7)
"""
       3
    9    20
  6    15   7

"""
r.left = rl
r.right = rr
rl.left = rll
rr.left = rrl
rr.right = rrr
s = Solution()
print(s.LevelOrderSuccessor(r))
