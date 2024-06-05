'''给你一个下标从 1 开始、长度为 n 的整数数组 nums 。

现定义函数 greaterCount ，使得 greaterCount(arr, val) 返回数组 arr 中 严格大于 val 的元素数量。

你需要使用 n 次操作，将 nums 的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：

如果 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr1 。
如果 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr2 。
如果 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) ，将 nums[i] 追加到元素数量较少的数组中。
如果仍然相等，那么将 nums[i] 追加到 arr1 。
连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。

返回整数数组 result 。

'''

class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 1
    def add(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t1 = Fenwick(m + 1)
        t2 = Fenwick(m + 1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            gc1 = len(a) - t1.pre(v)  # greaterCount(a, v)
            gc2 = len(b) - t2.pre(v)  # greaterCount(b, v)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                t1.add(v)
            else:
                b.append(x)
                t2.add(v)
        return a + b