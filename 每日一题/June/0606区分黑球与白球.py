'''桌子上有 n 个球，每个球的颜色不是黑色，就是白色。

给你一个长度为 n 、下标从 0 开始的二进制字符串 s，其中 1 和 0 分别代表黑色和白色的球。

在每一步中，你可以选择两个相邻的球并交换它们。

返回「将所有黑色球都移到右侧，所有白色球都移到左侧所需的 最小步数」。
'''
class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = cnt1 = 0
        for c in s:
            if c == '1':
                cnt1 += 1
            else:
                ans += cnt1
        return ans

# 遍历 s 的同时，统计 1 的个数 cnt1
# 遇到 0 时，这个 0 和它左边 cnt1个 111 都要交换，把 cnt1加入答案。
