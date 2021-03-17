"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
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
    def __init__(self):
        self.res = []

    def dfs(self, root, path):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:  # 如果到了叶子节点，就可以算作一个答案了
            self.res.append("->".join(path))
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        path.pop()  # 记得去掉这个递归的时候把当前加入的节点去掉

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.dfs(root, [])
        return self.res
