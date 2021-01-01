'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
from typing import List
from createtree import CreateTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []
    def trackback(self,root, target, res):
        if not root:
            return
        target = target - root.val
        if target == 0 and not root.left and not root.right:
            self.ans.append(res+[root.val])
            return
        self.trackback(root.left, target, res + [root.val])
        self.trackback(root.right, target, res + [root.val])
        return
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.trackback(root, sum, [])
        return self.ans


t = CreateTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
s=Solution()
print(s.pathSum(t,22))