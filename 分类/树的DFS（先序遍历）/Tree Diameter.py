"""
给定一棵二叉树，返回他从一个叶子节点到另一个叶子节点的最长路径
比如：
        1
    2       3
    4     5   6
最长的路径应该是5 [4 2 1 3 6]
         1
      2     3
          5    6
        7   8    9
            10     11
最长的路径应该是7 [10 8 5 3 6 9 11]
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_level(self, root):
        if root == None:
            return 0
        left = self.find_level(root.left)  # 递归找左子树的高度
        right = self.find_level(root.right)  # 递归找右子树的高度
        if left + right + 1 > self.treeDiameter:  # 更新答案
            self.treeDiameter = left + right + 1
        return max(left, right) + 1  # 左右子树最高的那个加上当前这个节点的高度

    def find_diameter(self, root):
        # 本质就是找到一个节点，这个节点的左右子树的高度和最大
        self.find_level(root)
        return self.treeDiameter


treeDiameter = TreeDiameter()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
