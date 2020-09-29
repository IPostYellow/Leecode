'''
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from createtree import CreateTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 递归方法,40ms,13.4MB
    def __init__(self):
        self.result = []

    def postorder(self, root):
        if root == None:
            return None
        else:
            if root.left:
                self.postorder(root.left)
            if root.right:
                self.postorder(root.right)
            self.result.append(root.val)

    def postorderTraversal(self, root):
        if root == None:
            return []
        else:
            self.postorder(root)
            return self.result


class Solution2:  # 递归方法,52ms,13.3MB
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root):
        stack = [root]
        if root == None:
            return []
        else:
            while (len(stack) > 0):
                tmp = stack[-1]
                if tmp == None:
                    stack.pop()
                    tmp = stack.pop()
                    self.result.append(tmp.val)
                    continue
                else:
                    stack.append(None)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)

        return self.result
t = CreateTree([3,1,2])
s=Solution2()
print(s.postorderTraversal(t))