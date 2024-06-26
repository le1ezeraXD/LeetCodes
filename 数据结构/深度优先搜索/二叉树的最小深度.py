'''给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
'''
from collections import deque


#DFS
def dfs(root):
    #首先设置两个先决条件
    #root节点为空则返回0
    if not root:
        return 0
    #如果root为叶子结点，返回1
    if not root.left and not root.right:
        return 1

    #设置最小深度depth
    depth = 10 ** 5
    if root.left:
        depth = min(dfs(root.left), depth)
    if root.right:
        depth = min(dfs(root.right), depth)

    return depth

def bfs(root):
    if not root:
        return 0
    #设置最小深度
    depth = 0
    #创建队列用来维护遍历出的节点
    que = deque([root])
    while que:
        size = len(que)
        for i in range(size):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            if not node.left and not node.right:
                depth += 1
                return depth
        depth += 1
    return depth

