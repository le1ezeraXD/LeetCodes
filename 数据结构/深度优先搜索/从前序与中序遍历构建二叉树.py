'''给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

作者：LeetCode
链接：https://leetcode.cn/leetbook/read/dfs/e8yiw6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1: i+1], inorder[:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

            return root