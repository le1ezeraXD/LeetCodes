'''给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。

你的任务是从范围 [0, n - 1] 内找出  2 个满足下述所有条件的下标 i 和 j ：

abs(i - j) >= indexDifference 且
abs(nums[i] - nums[j]) >= valueDifference
返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] ；否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。

注意：i 和 j 可能 相等 。
'''
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        #双层遍历，直接按照题目要求来写判断条件
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]