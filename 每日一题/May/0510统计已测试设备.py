'''2960.统计已测试设备
给你一个长度为 n 、下标从 0 开始的整数数组 batteryPercentages ，表示 n 个设备的电池百分比。

你的任务是按照顺序测试每个设备 i，执行以下测试操作：

如果 batteryPercentages[i] 大于 0：
增加 已测试设备的计数。
将下标在 [i + 1, n - 1] 的所有设备的电池百分比减少 1，确保它们的电池百分比 不会低于 0 ，即 batteryPercentages[j] = max(0, batteryPercentages[j] - 1)。
移动到下一个设备。
否则，移动到下一个设备而不执行任何测试。
返回一个整数，表示按顺序执行测试操作后 已测试设备 的数量。'''

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
    	#创建变量ans记录测试数量
        ans = 0
        #循环
        for i in range(len(batteryPercentages)):
        	#首先处理batteryPercentages中的元素
        	#根据题目得知每测试一个设备，这个被测试设备后面的设备电池百分比都会-1%
        	#又确保百分比不会低于0
        	#也就是每个电池百分比都要减去目前已经测试过的电池数量
        	#再与0做比较，取max值
            batteryPercentages[i] = max(batteryPercentages[i]-ans, 0)
            #如果处理后仍然大于0，则该设备被测试一次，ans加一
            if batteryPercentages[i] > 0:
                ans += 1
            #如果不大于0，则跳过不做任何处理
            else:
                continue
        
        return ans