# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import copy


class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, root, target, curSums, path):
        # 利用dfs将符合条件的路径存储起来就好了
        if not root:
            return
        curSums += root.val
        path.append(root.val)
        if not root.left and not root.right and target == curSums:
            self.ans.append(copy.deepcopy(path))
        if root.left:
            self.dfs(root.left, target, curSums, path)
        if root.right:
            self.dfs(root.right, target, curSums, path)
        curSums -= root.val
        path.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.dfs(root, sum, 0, [])
        return self.ans

r = TreeNode(3)
rl = TreeNode(9)
rr = TreeNode(20)
rll = TreeNode(18)
rrl = TreeNode(15)
rrr = TreeNode(7)
"""
       3
    9    20
  18    15   7

"""
r.left = rl
r.right = rr
rl.left = rll
rr.left = rrl
rr.right = rrr
s=Solution()
ans=s.pathSum(r,30)
print(ans)