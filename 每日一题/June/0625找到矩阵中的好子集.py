'''给你一个下标从 0 开始大小为 m x n 的二进制矩阵 grid 。

从原矩阵中选出若干行构成一个行的 非空 子集，如果子集中任何一列的和至多为子集大小的一半，那么我们称这个子集是 好子集。

更正式的，如果选出来的行子集大小（即行的数量）为 k，那么每一列的和至多为 floor(k / 2) 。

请你返回一个整数数组，它包含好子集的行下标，请你将子集中的元素 升序 返回。

如果有多个好子集，你可以返回任意一个。如果没有好子集，请你返回一个空数组。

一个矩阵 grid 的行 子集 ，是删除 grid 中某些（也可能不删除）行后，剩余行构成的元素集合。

'''

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        mask_to_idx = [-1] * (1 << n)
        for i, row in enumerate(grid):
            mask = 0
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0:
                return [i]
            mask_to_idx[mask] = i

        u = (1 << n) - 1
        for x, i in enumerate(mask_to_idx):
            if i < 0:
                continue
            y = c = u ^ x
            while y:
                j = mask_to_idx[y]
                if j >= 0:
                    return sorted((i, j))
                y = (y - 1) & c
        return []

'''
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        def good(nums1, nums2):
            for i in range(len(nums1)):
                if nums1[i] + nums2[i] > 1:
                    return False
            return True
        n = len(grid)
        if n == 1:
            return [] if sum(grid[0]) >= 1 else [0]
        if n == 0:
            return []
        for i in range(n):
            for j in range(i+1, n):
                if good(grid[i], grid[j]):
                    return [i, j]
        return []
'''