'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, left, right):
        if not left and not right:
            return True
        if left and right:
            if left.val == right.val:
                return self.DFS(left.left, right.right) and self.DFS(left.right, right.left)

        return False


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.DFS(root.left, root.right)