'''给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。

保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。

二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值 严格大于 Node.val。

二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。

作者：LeetCode
链接：https://leetcode.cn/leetbook/read/dfs/e8bv2c/
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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, left, right):
            if left > right:
                return None
            root = TreeNode(preorder[left])
            l, r = left, right
            while l < r:
                mid = l + (r - l + 1) // 2
                if preorder[mid] < preorder[left]:
                    l = mid
                else:
                    r = mid - 1

            leftTree = dfs(preorder, left + 1, l)
            rightTree = dfs(preorder, l + 1, right)
            root.left = leftTree
            root.right = rightTree
            return root

        n = len(preorder)
        if not n:
            return None
        return dfs(preorder, 0, n - 1)

