'''给定一个二进制数组 nums ，如果最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数。



示例 1：

输入：nums = [1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：4


提示:

1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res, prev = 0, 0
        cnt = 0
        for num in nums:
            #记录1的个数
            cnt += 1
            if num == 0:
                #如果遇到0 跳过这一次0 记录在这个0之前1的个数
                prev = cnt
                cnt = 0
            res = max(res, prev + cnt)
        return res
