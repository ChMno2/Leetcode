class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def unique(nums):
            nums = list(filter(lambda x : x != '.',nums))
            return len(set(nums)) == len(nums)
        SW = 9 #sudoku width
        GW = 3 #grid width
        for i in range(SW):
            if not unique(board[i]): #橫的
                return False
            if not unique([k[i] for k in board]): #直的
                return False
        for i in range(0,SW,GW): #九宮格
            for j in range(0,SW,GW):
                if not unique([board[i+m][j+k]for m in range(GW) for k in range(GW)]):
                    return False
        return True
