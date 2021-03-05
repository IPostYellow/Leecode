# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildtree(self,preorder,inorder,pb,pe,ib,ie)->TreeNode:
        if pb==pe:
            return None
        cur_node=TreeNode(preorder[pb])
        index=self.hashmap[preorder[pb]]
        cur_node.left=self.buildtree(preorder,inorder,pb+1,pb+index-ib+1,ib,index)
        cur_node.right=self.buildtree(preorder,inorder,pb+index-ib+1,pe,index+1,ie)
        return cur_node

    def buildTree(self, preorder, inorder) -> TreeNode:
        self.hashmap={}
        for i in range(len(inorder)):
            self.hashmap[inorder[i]]=i
        res= self.buildtree(preorder,inorder,0,len(preorder),0,len(inorder))
        # print(res.left.val)
        # print(res.left.left,res.left.right)
        # print(res.right.val)
        # print(res.right.left.val)
        # print(res.right.right.val)
        return res
# 法2
# Definition for a binary tree node.
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:1+i],inorder[:i])
        root.right=self.buildTree(preorder[1+i:],inorder[i+1:])
        return root
