'''给你一个下标从 0 开始的整数数组 nums 和一个正整数 x 。

你 一开始 在数组的位置 0 处，你可以按照下述规则访问数组中的其他位置：

如果你当前在位置 i ，那么你可以移动到满足 i < j 的 任意 位置 j 。
对于你访问的位置 i ，你可以获得分数 nums[i] 。
如果你从位置 i 移动到位置 j 且 nums[i] 和 nums[j] 的 奇偶性 不同，那么你将失去分数 x 。
请你返回你能得到的 最大 得分之和。

注意 ，你一开始的分数为 nums[0] 。
'''

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        @cache
        def dfs(i: int, j: int):
            if i == len(nums):
                return 0
            if nums[i] % 2 != j:
                return dfs(i+1, j)
            return max(dfs(i+1, j), dfs(i+1, j^1)-x) + nums[i]
        return dfs(0, nums[0] % 2)