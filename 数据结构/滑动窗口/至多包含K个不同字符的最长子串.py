'''给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长
子串
，并返回该子串的长度。


示例 1：

输入：s = "eceba"
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。
示例 2：

输入：s = "ccaabbb"
输出：5
解释：满足题目要求的子串是 "aabbb" ，长度为 5 。


提示：

1 <= s.length <= 105
s 由英文字母组成
'''
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 维护当前窗口中各个字母的个数
        map_num = defaultdict(int)
        # 维护当前窗口中不同字母个数
        kind = 0
        n = len(s)
        left = right = 0
        while right < n:
            #进right
            if map_num[s[right]] == 0:
                kind += 1
            map_num[s[right]] += 1
            #弹left
            if kind > 2:
                map_num[s[left]] -= 1
                # 处理left移动后，不同字母数可能会减少的。
                if map_num[s[left]] == 0: kind -= 1
                left += 1
            right += 1
        return right - left