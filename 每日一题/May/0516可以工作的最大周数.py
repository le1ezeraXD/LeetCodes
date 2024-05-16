'''给你 n 个项目，编号从 0 到 n - 1 。同时给你一个整数数组 milestones ，其中每个 milestones[i] 表示第 i 个项目中的阶段任务数量。

你可以按下面两个规则参与项目中的工作：

每周，你将会完成 某一个 项目中的 恰好一个 阶段任务。你每周都 必须 工作。
在 连续的 两周中，你 不能 参与并完成同一个项目中的两个阶段任务。
一旦所有项目中的全部阶段任务都完成，或者仅剩余一个阶段任务都会导致你违反上面的规则，那么你将 停止工作 。注意，由于这些条件的限制，你可能无法完成所有阶段任务。

返回在不违反上面规则的情况下你 最多 能工作多少周。'''

#老子每周都不想上班

def numberOfWeeks(milestones) -> int:
    #选出数组中最大值
    max_stone = max(milestones)
    #求和
    sum_stones = sum(milestones)
    #重点：
    #假设任务量最大的那天为第x天
    #那么想尽可能的消灭x天的任务，最有效率的办法是
    #做一天x天任务，再做一天其他任务，如此往复
    #所以将x天的任务全部做完，最少需要2*x天
    #如果这个数字小于所有项目数之和，说明在其他天任务都做完之前，第x天的任务就已经做完了
    #此时返回全部任务数量
    if 2 * max_stone <= sum_stones:
        return sum_stones
    #反之，则说明不能在不违反规则的情况下完成所有任务
    else:
        return (sum_stones-max_stone) * 2 + 1
    # return max_stone
    #简化版：速度更快，但费内存
    return sum_stones if 2 * max_stone <= sum_stones else ((sum_stones - max_stone) * 2 + 1)
print(numberOfWeeks([5,2,1]))