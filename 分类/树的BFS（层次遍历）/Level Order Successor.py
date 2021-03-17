"""
给定一棵树和其中的一个节点，判断其中那个节点的层次遍历的后继节点的值是多少
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def LevelOrderSuccessor(self, root: TreeNode, p):
        # 层次遍历每层求和即可
        if not root:
            return []
        q = deque()
        q.append(root)
        flag = 0
        while q:
            size = len(q)
            for i in range(size):
                tmp = q.popleft()
                if flag==1:
                    return tmp.val
                if tmp.val==p:
                    flag=1
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
        return -1

r = TreeNode(3)
rl = TreeNode(9)
rr = TreeNode(20)
rrl = TreeNode(15)
rrr = TreeNode(7)
"""
       3
    9     20
        15   7

"""
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr
s = Solution()
print(s.LevelOrderSuccessor(r,7))
