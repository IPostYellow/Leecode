"""
与Tree Diameter类似，只需要将层高改成当前层的权重就好了
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = -float("inf")

    def find_road_weight(self, root):
        if not root:
            return 0
        left = max(self.find_road_weight(root.left), 0)
        right = max(self.find_road_weight(root.right), 0)
        if left + right + root.val > self.res:
            self.res = left + right + root.val
        return max(left, right) + root.val

    def find_maximum_path_sum(self, root):
        self.find_road_weight(root)
        return self.res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print("Maximum Path Sum: " + str(s.find_maximum_path_sum(root)))
s = Solution()
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print("Maximum Path Sum: " + str(s.find_maximum_path_sum(root)))
s = Solution()
root = TreeNode(-1)
root.left = TreeNode(-3)
print("Maximum Path Sum: " + str(s.find_maximum_path_sum(root)))
