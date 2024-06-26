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
解释：满足题目要求的子串是 "aabbb" ，长度为 5 。'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 创建哈希表来维护窗口中各个字母数量
        map_num = defaultdict(int)
        # 创建变量kind维护当前窗口中不同字母个数
        kind = 0
        n = len(s)
        #初始化滑动窗口的两个边界值
        left = right = 0
        while right < n:
            #重点关注right
            #哈希表中没有right下标的字母时，kind加一代表出现了一个窗口中没有的字母
            if map_num[s[right]] == 0:
                kind += 1
            #map中对应value加一，代表该字母又出现一次
            map_num[s[right]] += 1
            #kind > 2代表窗口中有三种不同的字母，超出了题目限制
            if kind > 2:
            	#left下标的字母出现次数减一，left准备右移一位
                map_num[s[left]] -= 1
                # 处理left移动后，不同字母数可能会减少的。
                if map_num[s[left]] == 0: kind -= 1
                left += 1
            #无论如何right都要右移，所以不放在任何条件判断中
            right += 1
        return right - left