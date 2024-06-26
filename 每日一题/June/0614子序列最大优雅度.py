'''
给你一个长度为 n 的二维整数数组 items 和一个整数 k 。

items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。

现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。

你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。

用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。

注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。
'''

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda p: -p[0])
        ans = total_profit = 0
        vis = set()
        duplicate = []
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit
                if category not in vis:
                    vis.add(category)
                else:
                    duplicate.append(profit)
            elif duplicate and category not in vis:
                vis.add(category)
                total_profit += profit - duplicate.pop()
            ans = max(ans, total_profit + len(vis) * len(vis))
        return ans