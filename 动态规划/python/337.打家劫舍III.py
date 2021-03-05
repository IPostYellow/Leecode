class Solution:
    def rob(self, root: TreeNode) -> int:
        def robs(root):
            if root is None:
                return [0, 0]
            left = robs(root.left)
            right = robs(root.right)
            p1 = root.val + left[1] + right[1]
            p2 = max(left) + max(right)
            return [p1, p2]

        return max(robs(root))