"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 层次遍历每层求和即可
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            sums = 0
            for i in range(size):
                tmp = q.popleft()
                sums += tmp.val
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            res.append(sums / size)
        return res


r = TreeNode(3)
rl = TreeNode(9)
rr = TreeNode(20)
rrl = TreeNode(15)
rrr = TreeNode(7)
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr
s=Solution()
print(s.averageOfLevels(r))
