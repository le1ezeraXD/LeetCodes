'''给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。

最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。且必须从父节点到子节点，反过来是不可以的。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root) -> int:
        def dfs(p, parent, length):
            if not p: return length
            length = length + 1 if parent and p.val == parent.val + 1 else 1
            return max(length, max(dfs(p.left, p, length), dfs(p.right, p, length)))

        return dfs(root, None, 0)
