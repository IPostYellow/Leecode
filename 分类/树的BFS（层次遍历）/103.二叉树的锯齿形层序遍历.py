"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
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
    # 双端队列，奇数层左边出队，偶数层右边边出队
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que=deque()
        que.append(root)
        res=[]
        level=1
        while que:
            level_ans=[]
            level_size=len(que)
            if level%2==1: # 奇数层依然和正常的队列一样层次遍历
                for i in range(level_size):
                    tmp=que.popleft()
                    level_ans.append(tmp.val)
                    if tmp.left:
                        que.append(tmp.left)
                    if tmp.right:
                        que.append(tmp.right)
            else: #偶数层要从队列右边出队，然后从队列左边入队，注意的是，要先入队右节点
                for i in range(level_size):
                    tmp=que.pop()
                    level_ans.append(tmp.val)
                    if tmp.right:
                        que.appendleft(tmp.right)
                    if tmp.left:
                        que.appendleft(tmp.left)
            res.append(level_ans)
            level+=1
        return res