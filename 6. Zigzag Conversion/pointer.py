#利用step的正負值來控制row的移動方向
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        strings = ['' for _ in range(numRows)]
        row , step = 0,1
        for char in s:
            strings[row]+=char
            if row == numRows-1:
                step = -1
            elif row == 0:
                step = 1
            row +=step
        return ''.join(strings) 
