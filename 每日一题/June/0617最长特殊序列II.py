'''给定字符串列表 strs ，返回其中 最长的特殊序列 的长度。如果最长特殊序列不存在，返回 -1 。

特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。

 s 的 子序列可以通过删去字符串 s 中的某些字符实现。

例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
'''


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isequal(s1: str, s2: str):
            p1, p2 = 0, 0
            # if s1 == s2: return False
            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] == s2[p2]:
                    p1 += 1
                p2 += 1
            return p1 == len(s1)

        maxlen = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and isequal(s, t):
                    check = False
                    break
            if check:
                maxlen = max(maxlen, len(s))

        return maxlen
