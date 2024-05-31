'''
给你一个下标从 0 开始的二维整数矩阵 grid，大小为 n * n ，其中的值在 [1, n2] 范围内。除了 a 出现 两次，b 缺失 之外，每个整数都 恰好出现一次 。

任务是找出重复的数字a 和缺失的数字 b 。

返回一个下标从 0 开始、长度为 2 的整数数组 ans ，其中 ans[0] 等于 a ，ans[1] 等于 b
'''
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = []
        ans = [0] * (n*n)
        for i in range(n):
            for j in range(n):
                x = grid[i][j] - 1
                if ans[x] == 1:
                    res.append(x+1)
                ans[x] += 1

        for i in range(len(ans)):
            if ans[i] == 0:
                res.append(i+1)
        return res
