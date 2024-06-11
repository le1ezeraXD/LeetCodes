'''给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。

战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。
'''


class Solution:
    def countBattleships(board) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                #挨个遍历 如果遍历到X就向周围展开
                #当前元素上方为X 则继续遍历
                if i > 0 and board[i - 1][j] == 'X': continue
                if j > 0 and board[i][j - 1] == 'X': continue
                #当前元素周围没有X 则说明当前X为舰队首位 加一
                if board[i][j] == 'X':
                    res += 1

        return res
