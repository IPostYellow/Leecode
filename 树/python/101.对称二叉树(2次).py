'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from createtree import CreateTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # 递归方法 40ms,13.7mb
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):  # 判断左子树的左子树和右子树的右子树是否相同，左子树的右子树是否和右子树的左子树相同
            if left == None and right == None:
                return True
            if left != None and right == None:
                return False
            if left == None and right != None:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(right.left, left.right)

        if root == None:
            return True
        else:
            return dfs(root.left, root.right)


class Solution2:#32ms,13.7MB
    def isSymmetric(self, root: TreeNode) -> bool:
        def bfs(q1,q2):
            que =[q1,q2]
            while (que != []):
                t1=que.pop()
                t2=que.pop()
                if t1==None and t2==None:
                    continue
                if (t1==None and t2!=None) or (t1!=None and t2==None):
                    return False
                if t1.val!=t2.val:
                    return False
                que.append(t1.left)
                que.append(t2.right)

                que.append(t1.right)
                que.append(t2.left)

            return True

        return bfs(root,root)
#
#
# # [1,2,2,null,3,null,3]
# t = CreateTree([1, 2, 2, None, 3, None, 3])
#
# s=Solution2()
# print(s.isSymmetric(t))


#第二次
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_2:
    def isrevese(self,p,q):
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val==q.val:
            l=self.isrevese(p.left,q.right)
            l2=self.isrevese(p.right,q.left)
            return l and l2
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isrevese(root.left,root.right)


class Solution2_2:
    def isrevese(self, p, q):
        que = [p, q]
        while que:
            t1 = que.pop()
            t2 = que.pop()
            if (not t1 and t2) or (t1 and not t2):
                return False
            if not t1 and not t2:
                continue
            if t1.val != t2.val:
                return False
            que.append(t1.left)
            que.append(t2.right)

            que.append(t1.right)
            que.append(t2.left)

        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isrevese(root.left, root.right)