'''你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:

difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。

举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。



示例 1：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
示例 2:

输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0
'''

def maxProfitAssignment(difficulty, profits, workers) -> int:
    #使用二维数组将difficulty与profits一一对应
    jobs = sorted(zip(difficulty, profits))
    #将工人排序
    workers.sort()
    #ans为总利润数
    #j为快指针
    #max_profit记录当前工人对应的能拿到的最高利润
    #注：存在难度大工资低的情况，虽然很傻逼，但是要注意判断
    ans = j = max_profit = 0
    #遍历工人
    for w in workers:
        #针对当前工人，选取所能完成的最难的任务
        while j < len(jobs) and jobs[j][0] <= w:
            #因为存在难度大工资低的傻逼情况，所以要创建变量来维护可获得的最大利润
            max_profit = max(max_profit, jobs[j][1])
            #j指针前移
            j += 1
        ans += max_profit
    return ans